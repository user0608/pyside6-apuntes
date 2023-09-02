import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,  QWidget, QStackedLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent


class ColorBox(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack_layout = QStackedLayout()

        self.stack_layout.addWidget(ColorBox("orange"))
        self.stack_layout.addWidget(ColorBox("purple"))
        self.stack_layout.addWidget(ColorBox("magenta"))
        self.stack_layout.addWidget(ColorBox("gray"))
        self.stack_layout.addWidget(ColorBox("red"))

        self.mainwidget = QWidget()
        self.mainwidget.setLayout(self.stack_layout)

        self.setCentralWidget(self.mainwidget)
        self.resize(620, 480)

    def keyPressEvent(self, event: QKeyEvent):
        index = self.stack_layout.currentIndex()
        elements = self.stack_layout.count()
        match event.key():
            # case Qt.Key.Key_Up:
            #     print("key up")
            # case Qt.Key.Key_Down:
            #     print("key down")
            case Qt.Key.Key_Right:
                index += 1
            case Qt.Key.Key_Left:
                index -= 1

        if index < 0:
            index = elements-1
        if index >= elements:
            index = 0

        self.stack_layout.setCurrentIndex(index)

        return super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
