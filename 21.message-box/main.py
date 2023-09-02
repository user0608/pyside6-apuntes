from PySide6.QtWidgets import QApplication,  QMainWindow, QPushButton, QMessageBox
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):

        self.button = QPushButton("Show Dialog")
        self.button.clicked.connect(self.on_click)

        self.setCentralWidget(self.button)
        self.resize(480, 320)

    def on_click(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Soy el titulo")
        dialog.setText("Este es el texto del dialog")
        dialog.setStandardButtons(
            QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Close)

        dialog.button(QMessageBox.StandardButton.Apply).setText("Aplicar")

        dialog.setIcon(QMessageBox.Icon.Question)

        results = dialog.exec()
        if results == QMessageBox.StandardButton.Abort:
            print("Abort")
        if results == QMessageBox.StandardButton.Apply:
            print("Apply")
        if results == QMessageBox.StandardButton.Cancel:
            print("Cancel")
        if results == QMessageBox.StandardButton.Close:
            print("Close")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
