# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        font = QtGui.QFont()
        font.setPointSize(30)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 76))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        # Vars
        self.is_res = False

        # Label
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(180, 180, 180); color: #000000; padding: 1px")
        self.label.setObjectName("label")

        # Btn comma
        self.pushButton_comma = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_comma.setGeometry(QtCore.QRect(0, 394, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_comma.setFont(font)
        self.pushButton_comma.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_comma.setObjectName("pushButton_comma")

        # Btn 0
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(100, 394, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_0.setObjectName("pushButton_0")

        # Btn 1
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 288, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_1.setObjectName("pushButton_1")

        # Btn 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 288, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_2.setObjectName("pushButton_2")

        # Btn 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 288, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")

        self.pushButton_3.setObjectName("pushButton_3")

        # Btn 4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 182, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_4.setObjectName("pushButton_4")

        # Btn 5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 182, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_5.setObjectName("pushButton_5")

        # Btn 6
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 182, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_6.setObjectName("pushButton_6")

        # Btn 7
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 76, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_7.setObjectName("pushButton_7")

        # Btn 8
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 76, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_8.setObjectName("pushButton_8")

        # Btn 9
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 76, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_9.setObjectName("pushButton_9")

        # Btn 10
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(300, 182, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_minus.setObjectName("pushButton_minus")

        self.pushButton_multy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multy.setGeometry(QtCore.QRect(300, 288, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_multy.setFont(font)
        self.pushButton_multy.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_multy.setObjectName("pushButton_multy")

        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(300, 76, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_plus.setObjectName("pushButton_plus")

        self.pushButton_division = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_division.setGeometry(QtCore.QRect(300, 394, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_division.setFont(font)
        self.pushButton_division.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_division.setObjectName("pushButton_division")

        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(200, 394, 100, 106))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("QPushButton {background-color: rgb(210, 210, 210); border: solid\n} \
                                          QPushButton:hover{background-color: rgb(205, 205, 205);} \
                                          QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_equal.setObjectName("pushButton_equal")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_comma.setText(_translate("MainWindow", "."))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_multy.setText(_translate("MainWindow", "*"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_division.setText(_translate("MainWindow", "/"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))

        self.set_func()

    def set_func(self):
        self.pushButton_comma.clicked.connect(lambda: self.write_value(self.pushButton_comma.text()))
        self.pushButton_0.clicked.connect(lambda: self.write_value(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.write_value(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.write_value(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_value(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_value(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.write_value(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.write_value(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.write_value(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.write_value(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_value(self.pushButton_9.text()))
        self.pushButton_minus.clicked.connect(lambda: self.write_value(self.pushButton_minus.text()))
        self.pushButton_multy.clicked.connect(lambda: self.write_value(self.pushButton_multy.text()))
        self.pushButton_plus.clicked.connect(lambda: self.write_value(self.pushButton_plus.text()))
        self.pushButton_division.clicked.connect(lambda: self.write_value(self.pushButton_division.text()))
        self.pushButton_equal.clicked.connect(self.result)


    def write_value(self, value):
        if self.label.text() == '0' or self.is_res:
            if value in ['/', '*', '-', '+']:
                self.label.setText(self.label.text() + value)
            else:
                self.label.setText(value)

            self.is_res = False
        else:
            if value in ['/', '*', '-', '+'] and self.label.text()[-1] in ['/', '*', '-', '+']:
                pass
            else:
                self.label.setText(self.label.text() + value)

    def result(self):
        try:
            res = eval(self.label.text())
            print(res)
            self.label.setText(str(res))
        except (ZeroDivisionError, SyntaxError):
            self.label.setText('Ошибка')

        self.is_res = True



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
