from PySide6.QtWidgets import QApplication,  QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QDialogButtonBox
import sys


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Dialogo de prueba"))

        # buttonOK = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        # buttonCancel = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)

        # layout.addWidget(buttonOK)
        # layout.addWidget(buttonCancel)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        self.setLayout(layout)
        self.setWindowTitle("Soy un dialog")
        self.resize(240, 120)


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
        dialog = Dialog()
        result = dialog.exec()
        print(result)
        if result:
            print("Acepted")
        else:
            print("Rejected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
