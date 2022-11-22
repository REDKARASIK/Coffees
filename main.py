import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


def main():
    class CoffeeShow(QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('mainUI.ui', self)
            self.load_table()

        def load_table(self):
            self.coffee_table.setRowCount(0)

            with sqlite3.connect('coffee.sqlite3') as file:
                result = file.cursor().execute(
                    'select sorts.name, degree.name, coffees."ground/in grains", coffees.taste, '
                    'coffees.price, coffees.amount from coffees left join sorts on sorts.id = coffees.sort '
                    'left join degree on degree.id = coffees."degree of roasting"').fetchall()
                self.coffee_table.setColumnCount(len(result[0]))
                self.coffee_table.setHorizontalHeaderLabels(
                    ['Название сорта', 'Степень обжарки', 'Молотый/в зёрнах', 'Описание вкуса', 'Цена',
                     'Объём упаковки'])
                for i, row in enumerate(result):
                    self.coffee_table.setRowCount(self.coffee_table.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.coffee_table.setItem(i, j, QTableWidgetItem(str(elem)))

    app = QApplication(sys.argv)
    ex = CoffeeShow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
