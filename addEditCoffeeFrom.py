# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeFrom.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(615, 409)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 561, 331))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.sort_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sort_box.setObjectName("sort_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sort_box)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.degree_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.degree_box.setObjectName("degree_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.degree_box)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ground_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.ground_box.setObjectName("ground_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ground_box)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.taste_edit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.taste_edit.setObjectName("taste_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taste_edit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.amount_spin = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.amount_spin.setObjectName("amount_spin")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.amount_spin)
        self.price_spin = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.price_spin.setObjectName("price_spin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_spin)
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setGeometry(QtCore.QRect(510, 370, 93, 28))
        self.save_button.setObjectName("save_button")
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(50, 370, 431, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название сорта"))
        self.label_2.setText(_translate("Dialog", "Степень обжарки"))
        self.label_3.setText(_translate("Dialog", "Молотый/в зёрнах"))
        self.label_4.setText(_translate("Dialog", "Описание вкуса"))
        self.label_5.setText(_translate("Dialog", "Цена"))
        self.label_6.setText(_translate("Dialog", "Объём упаковки"))
        self.save_button.setText(_translate("Dialog", "Сохранить"))