import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget,  QHBoxLayout, QVBoxLayout


class ColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        horizontalLayout = QHBoxLayout()
        verticalLayout1 = QVBoxLayout()
        verticalLayout2 = QVBoxLayout()

        horizontalLayout.addWidget(ColorBox("green"))
        horizontalLayout.addLayout(verticalLayout1)
        horizontalLayout.addLayout(verticalLayout2)

        verticalLayout1.addWidget(ColorBox("blue"))
        verticalLayout1.addWidget(ColorBox("red"))

        verticalLayout2.addWidget(ColorBox("orange"))
        verticalLayout2.addWidget(ColorBox("magenta"))
        verticalLayout2.addWidget(ColorBox("purple"))

        self.mainwidget = QWidget()
        self.mainwidget.setLayout(horizontalLayout)
        self.setCentralWidget(self.mainwidget)
        self.resize(620, 480)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
