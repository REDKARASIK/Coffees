import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QDialog
from mainUI import Ui_MainWindow
from addEditCoffeeFrom import Ui_Dialog


def main():
    class ChangeCoffee(QDialog, Ui_Dialog):
        def __init__(self, id, sort, degree, ground, taste, price, amount):
            super().__init__()
            self.setupUi(self)
            self.id_sort = id
            self.sort = sort
            self.degree = degree
            self.ground = ground
            self.taste = taste
            self.price = price
            self.amount = amount
            self.make_comboboxes()
            self.fill_the_gasps()
            self.save_button.clicked.connect(self.change_coffees)

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

        def fill_the_gasps(self):
            self.sort_box.setCurrentIndex(self.sort_box.findText(self.sort))
            self.degree_box.setCurrentIndex(self.degree_box.findText(self.degree))
            self.ground_box.setCurrentIndex(self.ground_box.findText(self.ground))
            self.taste_edit.setText(self.taste)
            self.price_spin.setValue(float(self.price))
            self.amount_spin.setValue(float(self.amount))

        def change_coffees(self):
            self.error_label.setText('')
            price = float(self.price_spin.text().replace(',', '.'))
            amount = float(self.amount_spin.text().replace(',', '.'))
            if self.taste_edit.toPlainText() and price > 0 and amount > 0:
                text = self.taste_edit.toPlainText().replace('\n', '; ')
                with sqlite3.connect('coffee.sqlite3') as file:
                    file.cursor().execute('update coffees set sort = (select id from sorts where name = ?), '
                                          '"degree of roasting" = (select id from degree where name = ?),'
                                          ' "ground/in grains" = ?, taste = ?, price = ?, amount = ? where id = ?',
                                          (self.sort_box.currentText(), self.degree_box.currentText(),
                                           self.ground_box.currentText(),
                                           text, price, amount, self.id_sort))
                    file.commit()
                    self.done(1)
            else:
                self.error_label.setText('Неверно заполнена форма')

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
            price = float(self.price_spin.text().replace(',', '.'))
            amount = float(self.amount_spin.text().replace(',', '.'))
            if self.taste_edit.toPlainText() and price > 0 and amount > 0:
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
            self.change_button.clicked.connect(self.change_coffee)

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

        def change_coffee(self):
            if self.coffee_table.selectedItems():
                selected_row = self.coffee_table.currentRow()
                id_coffee = self.coffee_table.item(selected_row, 0).text()
                sort = self.coffee_table.item(selected_row, 1).text()
                degree = self.coffee_table.item(selected_row, 2).text()
                ground = self.coffee_table.item(selected_row, 3).text()
                taste = self.coffee_table.item(selected_row, 4).text()
                price = self.coffee_table.item(selected_row, 5).text()
                amount = self.coffee_table.item(selected_row, 6).text()
                dialog = ChangeCoffee(id_coffee, sort, degree, ground, taste, price, amount)
                dialog.show()
                if dialog.exec():
                    self.load_table()
                    print('Данные изменены')
                self.coffee_table.clearSelection()

    app = QApplication(sys.argv)
    ex = CoffeeShow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
