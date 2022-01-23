import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog
from .sha256_ui import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 实例化线程对象
        self.work = WorkThread()
        self.pushButton.clicked.connect(self.open_dir)
        self.pushButton_2.clicked.connect(self.execute)

    def open_dir(self):
        file_path = QFileDialog.getExistingDirectory(self, "选取指定文件夹", "C:/")
        if file_path:
            self.lineEdit.setText(file_path)

    def execute(self):
        if self.lineEdit.text():
            # 启动线程
            self.work.start()
            # 线程自定义信号连接的槽函数
            self.work.started.connect(self.start)
            self.work.trigger.connect(self.display)
            self.work.finished.connect(self.end)
        else:
            QMessageBox.warning(self, "警告对话框", "请先选择文件夹")

    def start(self):
        # 线程开始的处理
        self.plainTextEdit.addItem(f">>>>>>>>>>>>all start<<<<<<<<<<<<<<")

    def display(self, params):
        # 由于自定义信号时自动传递一个参数对象
        self.plainTextEdit.addItem(f"{params['prefix']}:{params['line']}")

    def end(self):
        # 线程结束的处理
        self.plainTextEdit.addItem(f">>>>>>>>>>>>all finished<<<<<<<<<<<<<<")


class WorkThread(QThread):
    # 自定义信号对象。参数dict就代表这个信号可以传一个dict对象
    trigger = pyqtSignal(dict)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
        # 重写线程执行的run函数
        # 触发自定义信号
        choosed_dir = self.lineEdit.text()
        for i in range(20):
            self.trigger.emit({"prefix": "start", "line": f"{str(i)} - {choosed_dir}"})
            time.sleep(1)
            # 通过自定义信号把待显示的字符串传递给槽函数
            self.trigger.emit({"prefix": "end", "line": f"{str(i)} - {choosed_dir}"})


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
