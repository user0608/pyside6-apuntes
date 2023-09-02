import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class CustomBoxWitget(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.caja = CustomBoxWitget("green")
        self.setCentralWidget(self.caja)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
