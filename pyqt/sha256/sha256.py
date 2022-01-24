import sys
import os
import hashlib
import time
import cgitb
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog
from .sha256_ui import *


class MainWindow(QMainWindow, Ui_SHA256):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 定义button的槽函数
        self.pushButton.clicked.connect(self.open_dir)
        self.pushButton_2.clicked.connect(self.execute)

    def open_dir(self):
        file_path = QFileDialog.getExistingDirectory(self, "选取指定文件夹", "C:/")
        if file_path:
            self.lineEdit.setText(file_path)

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

    def start(self):
        # 线程开始的处理
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f">>>>>all start<<<<<")

    def display(self, params):
        # 由于自定义信号时自动传递一个参数对象
        self.plainTextEdit.appendPlainText(f"{params['prefix']}:{params['line']}")

    def warn(self):
        # 显示警告
        QMessageBox.warning(self, "警告对话框", "该文件夹不存在，请重新选择!")

    def end(self):
        # 线程结束的处理
        self.plainTextEdit.appendPlainText(f">>>>>all finished<<<<<<")


class WorkThread(QThread):
    # 自定义信号对象，无参数
    warn_signal = pyqtSignal()
    # 自定义信号对象，参数dict就代表这个信号可以传一个dict对象
    trigger = pyqtSignal(dict)

    def __init__(self, choose_dir: str = None):
        # 初始化函数
        super().__init__()
        self.choose_dir = choose_dir

    def run(self):
        # 重写线程执行的run函数，触发自定义信号
        if not os.path.isdir(self.choose_dir):
            self.warn_signal.emit()
            return
        for i, file in enumerate(os.listdir(self.choose_dir)):
            if file.endswith(".json"):
                self.trigger.emit({"prefix": "start", "line": f"{file}"})
                # time.sleep(1)
                file_name, ext = os.path.splitext(file)
                chk_file_name = f"{file_name}.chk"
                with open(os.path.join(self.choose_dir, file), "rb") as f:
                    bs = f.read()  # read entire file as bytes
                    chk_value = hashlib.sha256(bs).hexdigest()
                with open(os.path.join(self.choose_dir, chk_file_name), 'w') as f:
                    f.write(chk_value)
                self.trigger.emit({"prefix": "end", "line": f"{file}"})


def main():
    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setFixedSize(main_window.width(), main_window.height())
    main_window.show()
    sys.exit(app.exec_())
