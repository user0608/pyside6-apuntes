from PySide6.QtWidgets import QApplication,   QMainWindow, QSpinBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.number = QSpinBox()
        self.setCentralWidget(self.number)
        # self.number.setMinimum(55)
        # self.number.setMaximum(1000)
        self.number.setRange(55, 1000)
        self.number.setSingleStep(10)
        self.number.setSuffix("%")
        self.number.valueChanged.connect(self.on_change)

    def on_change(self, value):
        print(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
