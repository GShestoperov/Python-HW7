# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task34.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 155)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leInputStr = QtWidgets.QLineEdit(self.centralwidget)
        self.leInputStr.setGeometry(QtCore.QRect(250, 10, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leInputStr.setFont(font)
        self.leInputStr.setObjectName("leInputStr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btCheck = QtWidgets.QPushButton(self.centralwidget)
        self.btCheck.setGeometry(QtCore.QRect(330, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btCheck.setFont(font)
        self.btCheck.setObjectName("btCheck")
        self.lbResult = QtWidgets.QLabel(self.centralwidget)
        self.lbResult.setGeometry(QtCore.QRect(30, 90, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbResult.setFont(font)
        self.lbResult.setStyleSheet("")
        self.lbResult.setText("")
        self.lbResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lbResult.setObjectName("lbResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Задача 34: про стих Винни-пуха"))
        self.leInputStr.setText(_translate("MainWindow", "пара-ра-рюм-да рам-ра-пам-папом па-ра-пе-да па-ра-пим-да"))
        self.label.setText(_translate("MainWindow", "Введите стих Винни-пуха:"))
        self.btCheck.setText(_translate("MainWindow", "Проверить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
