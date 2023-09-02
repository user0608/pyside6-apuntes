from PySide6.QtWidgets import QApplication,  QMainWindow, QPushButton, QDialog
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.resize(480, 320)

        self.button = QPushButton("Show Dialog")
        self.button.clicked.connect(self.on_click)

        self.setCentralWidget(self.button)

    def on_click(self):
        dialog = QDialog()
        dialog.setWindowTitle("Soy un dialog")
        dialog.exec()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
