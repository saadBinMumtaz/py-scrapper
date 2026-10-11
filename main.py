import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QLineEdit, QPushButton,
    QFormLayout, QMessageBox, QAbstractItemView,
)
from data_store import FIELDS, load_rows, save_rows, next_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project 1 - CRUD")
        self.resize(1000, 600)
        self.rows = load_rows() 
        self.selected_index = None 
        
        # ----- table -----
        self.table = QTableWidget()
        self.table.setColumnCount(len(FIELDS))
        self.table.setHorizontalHeaderLabels(FIELDS)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellClicked.connect(self.on_row_clicked)

        # ----- form (one text box per column, except id) -----
        self.inputs = {}
        form = QFormLayout()
        for name in FIELDS:
            if name == "id":
                continue
            box = QLineEdit()
            self.inputs[name] = box
            form.addRow(name.capitalize(), box)

        # ----- buttons -----
        add_btn = QPushButton("Add")
        add_btn.clicked.connect(self.add_row)

        buttons = QHBoxLayout()
        buttons.addWidget(add_btn)

        side = QVBoxLayout()
        side.addLayout(form)
        side.addLayout(buttons)
        side.addStretch()
        side_widget = QWidget()
        side_widget.setLayout(side)

        # ----- table on the left, form on the right -----
        main = QHBoxLayout()
        main.addWidget(self.table, 3)
        main.addWidget(side_widget, 1)
        central = QWidget()
        central.setLayout(main)
        self.setCentralWidget(central)

        self.refresh_table()
        
    def refresh_table(self):
        self.table.setRowCount(len(self.rows))
        for r, row in enumerate(self.rows):
            for c, name in enumerate(FIELDS):
                self.table.setItem(r, c, QTableWidgetItem(str(row.get(name, ""))))

    def read_form(self):
        """Get values from the boxes. Returns None if something is empty."""
        data = {name: box.text().strip() for name, box in self.inputs.items()}
        if any(v == "" for v in data.values()):
            QMessageBox.warning(self, "Missing data", "Please fill all fields.")
            return None
        return data

    def clear_form(self):
        for box in self.inputs.values():
            box.clear()
        self.selected_index = None
        self.table.clearSelection()

    def add_row(self):                                  
        data = self.read_form()
        if data is None:
            return
        data["id"] = next_id(self.rows)
        self.rows.append(data)
        save_rows(self.rows)
        self.refresh_table()
        self.clear_form()
        
    def on_row_clicked(self, row, _col):                 # READ (show in form)
        self.selected_index = row
        for name, box in self.inputs.items():
            box.setText(str(self.rows[row][name]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())