from PySide6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)
window = QWidget()
window.show()

if __name__ == "__main__":
    sys.exit(app.exec())
