# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.circlesButton = QtWidgets.QPushButton(Form)
        self.circlesButton.setGeometry(QtCore.QRect(184, 20, 131, 23))
        self.circlesButton.setObjectName("circlesButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Случайные круги"))
        self.circlesButton.setText(_translate("Form", "Нажми на меня!"))
