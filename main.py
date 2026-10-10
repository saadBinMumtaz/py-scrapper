import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QTableWidget,
)
from data_store import FIELDS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project 1 - CRUD")
        self.resize(1000, 600)

        # ----- table -----
        self.table = QTableWidget()
        self.table.setColumnCount(len(FIELDS))
        self.table.setHorizontalHeaderLabels(FIELDS)
        self.table.horizontalHeader().setStretchLastSection(True)

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())