import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QAbstractItemView,
)
from data_store import FIELDS, load_rows


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project 1 - CRUD")
        self.resize(1000, 600)
        self.rows = load_rows() 

        # ----- table -----
        self.table = QTableWidget()
        self.table.setColumnCount(len(FIELDS))
        self.table.setHorizontalHeaderLabels(FIELDS)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.refresh_table()
        
    def refresh_table(self):
        self.table.setRowCount(len(self.rows))
        for r, row in enumerate(self.rows):
            for c, name in enumerate(FIELDS):
                self.table.setItem(r, c, QTableWidgetItem(str(row.get(name, ""))))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())