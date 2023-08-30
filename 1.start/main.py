from PySide6.QtWidgets import QApplication,  QPushButton, QMainWindow
import sys


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Hola, soy el titulo")

button = QPushButton("Tocame")
window.setCentralWidget(button)

window.show()

if __name__ == "__main__":
    sys.exit(app.exec())
