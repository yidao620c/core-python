import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog
from .sha256_ui import *


class MainWindow(QMainWindow, Ui_MainWindow):
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
            self.plainTextEdit.appendPlainText(f"11111111111111")
            self.plainTextEdit.appendPlainText(f"22222222222222")

    def execute(self):
        if self.lineEdit.text():
            # 实例化线程对象
            work = WorkThread(choose_dir=self.lineEdit.text())
            # 线程自定义信号连接的槽函数
            work.started.connect(self.start)
            work.trigger.connect(self.display)
            work.finished.connect(self.end)
            # 启动线程
            work.start()
        else:
            QMessageBox.warning(self, "警告对话框", "请先选择文件夹")

    def start(self):
        # 线程开始的处理
        self.plainTextEdit.appendPlainText(f">>>>>>>>>>>>all start<<<<<<<<<<<<<<")

    def display(self, params):
        # 由于自定义信号时自动传递一个参数对象
        self.plainTextEdit.appendPlainText(f"{params['prefix']}:{params['line']}")

    def end(self):
        # 线程结束的处理
        self.plainTextEdit.appendPlainText(f">>>>>>>>>>>>all finished<<<<<<<<<<<<<<")


class WorkThread(QThread):
    # 自定义信号对象。参数dict就代表这个信号可以传一个dict对象
    trigger = pyqtSignal(dict)

    def __init__(self, choose_dir: str = None):
        # 初始化函数
        super().__init__()
        self.choose_dir = choose_dir

    def run(self):
        # 重写线程执行的run函数，触发自定义信号
        for i in range(20):
            self.trigger.emit({"prefix": "start", "line": f"{str(i)} - {self.choose_dir}"})
            time.sleep(1)
            # 通过自定义信号把待显示的字符串传递给槽函数
            self.trigger.emit({"prefix": "end", "line": f"{str(i)} - {self.choose_dir}"})


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
