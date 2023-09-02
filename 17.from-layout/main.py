import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,  QWidget, QFormLayout
from PySide6.QtCore import Qt


class ColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        form = QFormLayout()

        form.addRow("Naranja", ColorBox("orange"))
        form.addRow("Morado", ColorBox("purple"))
        form.addRow("Magentas", ColorBox("magenta"))
        form.addRow("Gris", ColorBox("gray"))
        form.addRow("Rojo", ColorBox("red"))

        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
    
        self.mainwidget = QWidget()
        self.mainwidget.setLayout(form)

        self.setCentralWidget(self.mainwidget)
        self.resize(620, 480)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
