from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel,  QWidget,
    QPushButton, QFormLayout, QCheckBox, QRadioButton, QLineEdit, QDateEdit,
    QDateTimeEdit, QSpinBox, QDoubleSpinBox, QComboBox, QFontComboBox, QProgressBar,
    QLCDNumber, QSlider, QDial
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
import sys


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
    app.setStyle("Fusion")

    dark_fusion = QPalette()
    dark_fusion.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    dark_fusion.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ColorRole.ToolTipBase, QColor(25, 25, 25))
    dark_fusion.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    dark_fusion.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    dark_fusion.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    dark_fusion.setColor(QPalette.ColorRole.BrightText, Qt.red)
    dark_fusion.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    dark_fusion.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))

    dark_fusion.setColor(
        QPalette.ColorRole.HighlightedText, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.ColorGroup.Active,
                         QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ColorGroup.Disabled,
                         QPalette.ColorRole.ButtonText, Qt.GlobalColor.darkGray)
    dark_fusion.setColor(QPalette.ColorGroup.Disabled,
                         QPalette.ColorRole.WindowText, Qt.GlobalColor.darkGray)
    dark_fusion.setColor(QPalette.ColorGroup.Disabled,
                         QPalette.ColorRole.Text, Qt.GlobalColor.darkGray)
    dark_fusion.setColor(QPalette.ColorGroup.Disabled,
                         QPalette.ColorRole.Light, QColor(53, 53, 53))

    app.setPalette(dark_fusion)

    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
