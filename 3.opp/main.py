from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        button = QPushButton("Tocame")
        self.setCentralWidget(button)
        self.setWindowTitle("Hola Mundo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
