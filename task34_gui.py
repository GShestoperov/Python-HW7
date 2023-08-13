# Задача 36 с графическим интерфейсом

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from task34_ui import Ui_MainWindow


class Task34Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Task34Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.btCheck.clicked.connect(self.checkRhyme)

    def checkRhyme(self):
        result = True

        data_str = self.ui.leInputStr.text().lower()
        data_list = data_str.split()
        data = list(enumerate(data_list))
        data_first = list(filter(lambda item: item[0] % 2 == 0, data))
        data_second = list(filter(lambda item: item[0] % 2 != 0, data))

        for index in range(min(len(data_first), len(data_second))):
            vowel_count_first = 0
            vowel_count_second = 0

            for ch in "аеийоуыэюя":
                vowel_count_first += data_first[index][1].count(ch)
                vowel_count_second += data_second[index][1].count(ch)

            if vowel_count_first != vowel_count_second:
                result = False
                break

        if result:
            self.ui.lbResult.setText("УРА! Парам пам-пам")
            self.ui.lbResult.setStyleSheet("background-color: green;")
        else:
            self.ui.lbResult.setText("Увы, Пам парам")
            self.ui.lbResult.setStyleSheet("background-color: red;")


app = QtWidgets.QApplication([])
application = Task34Application()
application.show()

sys.exit(app.exec())
