from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QColor
from dataLoader import loadData

state = {}
ui = {}

def fillTable(rows, sortCol=-1):
    table = ui["table"]
    table.clearContents()
    table.setRowCount(len(rows))

    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            item = QTableWidgetItem(str(value))

            if j == sortCol:
                item.setBackground(QColor("#2a2a3d"))

            table.setItem(i, j, item)


def buildWindow():
    cols, kinds, rows = loadData("data/spotify_songs.csv")

    state["cols"] = cols
    state["kinds"] = kinds
    state["full"] = rows
    state["shown"] = rows

    win = QMainWindow()
    win.setWindowTitle("Data Sorter")
    win.resize(1300, 750)

    table = QTableWidget()
    table.setColumnCount(len(cols))
    table.setHorizontalHeaderLabels(cols)
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.setAlternatingRowColors(True)

    ui["win"] = win
    ui["table"] = table

    win.setCentralWidget(table)
    fillTable(rows)

    return win