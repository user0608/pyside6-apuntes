from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel,  QWidget,
    QPushButton, QFormLayout, QLineEdit,  QSpinBox,
)
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        form = QFormLayout()
        form.addRow("QPushButton", QPushButton("QPushButton"))
        form.addRow("QLineEdit", QLineEdit("QLineEdit"))
        form.addRow("QSpinBox", QSpinBox())

        etiqueta = QLabel("QLabel")
        etiqueta.setObjectName("etiqueta")
        form.addRow(etiqueta)

        widget = QWidget()
        widget.setLayout(form)
        self.setCentralWidget(widget)

        self.setStyleSheet(
            """
                QMainWindow {
                    background-color:#212121
                }
                QLabel {
                    color: #e9e9e9
                }
                QPushButton {
                    background-color: orange;
                    font-family: "Arial";
                    font-size:14px;
                    font-weight: bold;
                }
                #etiqueta {
                    background-color:cyan;
                    padding:10px;
                    color:black;
                }
            """
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
