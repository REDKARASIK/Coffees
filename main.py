import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QDialog
from mainUI import Ui_MainWindow
from addEditCoffeeFrom import Ui_Dialog


def main():
    class AddCoffee(QDialog, Ui_Dialog):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.make_comboboxes()

        def make_comboboxes(self):
            with sqlite3.connect('coffee.sqlite3') as file:
                # Combobox_sort
                result = file.cursor().execute('select sorts.name from sorts').fetchall()
                for i in result:
                    self.sort_box.addItem(*i)
                # Combobox_degree
                result = file.cursor().execute('select degree.name from degree').fetchall()
                for i in result:
                    self.degree_box.addItem(*i)
                # Grounded_box
                self.ground_box.addItem('0')
                self.ground_box.addItem('1')

    class CoffeeShow(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.load_table()
            self.coffee_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.add_button.clicked.connect(self.add_coffee)

        def load_table(self):
            self.coffee_table.setRowCount(0)

            with sqlite3.connect('coffee.sqlite3') as file:
                result = file.cursor().execute(
                    'select coffees.id, sorts.name, degree.name, coffees."ground/in grains", coffees.taste, '
                    'coffees.price, coffees.amount from coffees left join sorts on sorts.id = coffees.sort '
                    'left join degree on degree.id = coffees."degree of roasting"').fetchall()
                self.coffee_table.setColumnCount(len(result[0]))
                self.coffee_table.setHorizontalHeaderLabels(
                    ['ИД', 'Название сорта', 'Степень обжарки', 'Молотый/в зёрнах', 'Описание вкуса', 'Цена',
                     'Объём упаковки'])
                for i, row in enumerate(result):
                    self.coffee_table.setRowCount(self.coffee_table.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.coffee_table.setItem(i, j, QTableWidgetItem(str(elem)))

        def add_coffee(self):
            dialog = AddCoffee()
            dialog.show()
            if dialog.exec():
                print('Данные изменены')

    app = QApplication(sys.argv)
    ex = CoffeeShow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
