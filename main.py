import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import buildWindow

app = QApplication(sys.argv)
win = buildWindow()
win.show()
sys.exit(app.exec())