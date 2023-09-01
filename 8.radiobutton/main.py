from PySide6.QtWidgets import QApplication,   QMainWindow, QRadioButton
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.button = QRadioButton("Radio")
        self.button.setChecked(True)
        self.button.toggled.connect(self.on_chanage)
        self.setCentralWidget(self.button)

    def on_chanage(self, value):
        print(value)
        if self.button.isChecked():
            print("Esta marcado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
