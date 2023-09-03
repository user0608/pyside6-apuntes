from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel,  QWidget,
    QPushButton, QFormLayout, QCheckBox, QRadioButton, QLineEdit, QDateEdit,
    QDateTimeEdit, QSpinBox, QDoubleSpinBox, QComboBox, QFontComboBox, QProgressBar,
    QLCDNumber, QSlider, QDial, QStyle
)
from PySide6.QtCore import Qt
import sys
from qt_material import apply_stylesheet


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Form")
        form = QFormLayout()
        form.addRow("QCheckBox", QCheckBox())
        form.addRow("QRadioButton", QRadioButton())
        form.addRow("QLabel", QLabel("QLabel"))
        form.addRow("QPushButton", QPushButton("QPushButton"))
        form.addRow("QLineEdit", QLineEdit("QLineEdit"))
        form.addRow("QDateEdit", QDateEdit())
        form.addRow("QDateTimeEdit", QDateTimeEdit())
        form.addRow("QSpinBox", QSpinBox())
        form.addRow("QDoubleSpinBox", QDoubleSpinBox())
        form.addRow("QComboBox", QComboBox())
        form.addRow("QFontComboBox", QFontComboBox())
        form.addRow("QProgressBar", QProgressBar())
        form.addRow("QLCDNumber", QLCDNumber())
        form.addRow("QSlider", QSlider(Qt.Orientation.Horizontal))
        form.addRow("QDial", QDial())

        widget = QWidget()
        widget.setLayout(form)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'light_red.xml')
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
