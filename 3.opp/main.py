from PySide6.QtWidgets import QApplication,  QPushButton, QMainWindow
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        button = QPushButton("Tocame")
        self.setCentralWidget(button)
        self.setWindowTitle("Hola Mundo")
        self.setMinimumSize(QSize(620, 480))
        self.setMaximumSize(QSize(820, 580))
        # self.setFixedSize(QSize(820, 580)) # no redimensionale


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
