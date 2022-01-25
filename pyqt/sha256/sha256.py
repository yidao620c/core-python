import sys
import os
import hashlib
import time
import cgitb
from PyQt5.QtCore import QThread, pyqtSignal, QBasicTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, \
    QLabel, QProgressBar
from .sha256_ui import *


class MainWindow(QMainWindow, Ui_SHA256):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.post_setupUi()

    def post_setupUi(self):
        """designer设计之后的自定义UI设计"""
        # 定义文本标签
        self.statusLabel = QLabel()
        # 设置文本标签显示内容
        self.statusLabel.setText("  准备")
        # 定义水平进度条
        self.progressBar = QProgressBar()
        # 设置进度条的范围，参数1为最小值，参数2为最大值（可以调得更大，比如1000）
        self.progressBar.setRange(0, 100)
        # 设置进度条的初始值
        self.progressBar.setValue(0)
        # 设置定时器（走进度条的时候需要使用，否则进度条不会变化，而是固定不变）
        self.timer = QBasicTimer()
        self.step = 0
        # 往状态栏中添加组件（stretch是拉伸组件宽度）
        self.statusBar.addPermanentWidget(self.statusLabel, stretch=2)
        self.statusBar.addPermanentWidget(self.progressBar, stretch=20)
        # 定义button的槽函数
        self.pushButton.clicked.connect(self.open_dir)
        self.pushButton_2.clicked.connect(self.btn_action)

    # 每一个QObject对象或其子对象都有一个QObject.timerEvent方法。
    # 为了响应定时器的超时事件，需要重写进度条的timerEvent方法。
    def timerEvent(self, event):
        # 累计步数
        self.step = max(self.progressBar.value(), self.step) + 1
        if self.step >= 100:
            self.step = 0
        # 修改进度条的值
        self.progressBar.setValue(self.step)

    def open_dir(self):
        file_path = QFileDialog.getExistingDirectory(self, "选取指定文件夹")
        if file_path:
            self.lineEdit.setText(file_path)

    def btn_action(self):
        if self.pushButton_2.text() == "开始":
            self.execute()
        else:
            self.cancel()

    def execute(self):
        if self.lineEdit.text():
            # 实例化线程对象，注意之类一定要设置成成员变量self，因为生命周期原因
            self.work = WorkThread(choose_dir=self.lineEdit.text())
            # 线程自定义信号连接的槽函数
            self.work.started.connect(self.start)
            self.work.trigger.connect(self.display)
            self.work.warn_signal.connect(self.warn)
            self.work.finished.connect(self.end)
            # 启动线程
            self.work.start()
        else:
            QMessageBox.warning(self, "警告对话框", "请先选择文件夹")

    def cancel(self):
        if self.work:
            if QMessageBox.Yes == QMessageBox.question(
                    self, "确认对话框", "你确定要取消吗？", QMessageBox.Yes | QMessageBox.No):
                self.work.stop()
                self.timer.stop()

    def start(self):
        # 线程开始的处理
        # self.pushButton_2.setEnabled(False)
        self.pushButton_2.setText("取消")
        self.statusLabel.setText(" 执行中")
        self.progressBar.setValue(0)
        # 使用定时器的start()方法启动定时器，激活进度条。其中：
        # 参数1：超时时间；参数2：到了超时时间后，接收定时器触发超时事件的对象。
        self.timer.start(500, self)
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f">>>>>all start<<<<<")

    def display(self, params):
        # 由于自定义信号时自动传递一个参数对象
        self.plainTextEdit.appendPlainText(f"{params['prefix']}:{params['line']}")
        if "progress" in params:
            self.progressBar.setValue(max(params['progress'], self.progressBar.value()))

    def warn(self):
        # 显示警告
        QMessageBox.warning(self, "警告对话框", "该文件夹不存在，请重新选择!")

    def end(self):
        # 线程结束的处理
        self.plainTextEdit.appendPlainText(f">>>>>all finished<<<<<<")
        self.statusLabel.setText(" 准备")
        self.pushButton_2.setText("开始")
        self.progressBar.setValue(0)
        self.timer.stop()
        # self.pushButton_2.setEnabled(True)


class WorkThread(QThread):
    # 自定义信号对象，无参数
    warn_signal = pyqtSignal()
    # 自定义信号对象，参数dict就代表这个信号可以传一个dict对象
    trigger = pyqtSignal(dict)
    # 自定义开始和结束信号
    start_signal = pyqtSignal(bool)

    def __init__(self, choose_dir: str = None):
        # 初始化函数
        super().__init__()
        self.choose_dir = choose_dir
        self._is_running = True

    def run(self):
        # 重写线程执行的run函数，触发自定义信号
        if not os.path.isdir(self.choose_dir):
            self.warn_signal.emit()
            return
        all_files = list(filter(lambda f: f.endswith('.json'), os.listdir(self.choose_dir)))
        count = 0
        for i, file in enumerate(all_files):
            if not self._is_running:
                break
            if file.endswith(".json"):
                self.trigger.emit({"prefix": "start", "line": f"{file}"})
                time.sleep(2)
                file_name, ext = os.path.splitext(file)
                chk_file_name = f"{file_name}.chk"
                with open(os.path.join(self.choose_dir, file), "rb") as f:
                    bs = f.read()  # read entire file as bytes
                    chk_value = hashlib.sha256(bs).hexdigest()
                with open(os.path.join(self.choose_dir, chk_file_name), 'w') as f:
                    f.write(chk_value)
                count += 1
                self.trigger.emit(
                    {"prefix": "end", "line": f"{file}", "progress": count * 100 / len(all_files)})

    def stop(self):
        self._is_running = False


def main():
    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setFixedSize(main_window.width(), main_window.height())
    main_window.show()
    sys.exit(app.exec_())
