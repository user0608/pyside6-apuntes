from PySide6.QtWidgets import QApplication,   QMainWindow, QListWidget
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.list = QListWidget()
        self.list.addItems(["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"])
        self.list.currentItemChanged.connect(self.on_item_change)
        self.list.currentTextChanged.connect(self.on_text_change)
        self.setCentralWidget(self.list)

    def on_item_change(self, item):
        print(item)

    def on_text_change(self, value):
        print(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
