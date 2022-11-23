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
            self.save_button.clicked.connect(self.add_coffee)

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

        def add_coffee(self):
            self.error_label.setText('')
            price = self.price_spin.text().replace(',', '.')
            amount = self.amount_spin.text().replace(',', '.')
            if self.taste_edit.toPlainText() and float(price) > 0 and float(amount) > 0:
                text = self.taste_edit.toPlainText().replace('\n', '; ')
                with sqlite3.connect('coffee.sqlite3') as file:
                    file.cursor().execute('insert into coffees(sort, "degree of roasting", "ground/in grains", taste,'
                                          ' price, amount) values ((select id from sorts where sorts.name = ?),'
                                          ' (select id from degree where degree.name = ?), ?, ?, ?, ?)',
                                          (self.sort_box.currentText(), self.degree_box.currentText(),
                                           self.ground_box.currentText(), text, price, amount))
                    file.commit()
                self.done(1)
            else:
                self.error_label.setText('Неверно заполнена форма')

    class CoffeeShow(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.load_table()
            self.coffee_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.add_button.clicked.connect(self.add_coffee)
            self.delete_button.clicked.connect(self.delete_coffee)

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
                self.load_table()
                print('Данные изменены')

        def delete_coffee(self):
            if self.coffee_table.selectedItems():
                id_coffee = self.coffee_table.item(self.coffee_table.currentRow(), 0).text()
                with sqlite3.connect('coffee.sqlite3') as file:
                    file.cursor().execute('delete from coffees where id = ?;', (id_coffee,))
                    file.commit()
                self.coffee_table.clearSelection()
                self.load_table()
                print('Данные изменены')

    app = QApplication(sys.argv)
    ex = CoffeeShow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
