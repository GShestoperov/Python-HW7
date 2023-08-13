# Задача 36 с графическим интерфейсом

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from task36_ui import Ui_MainWindow


class Task36Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Task36Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.btGenerateTable.clicked.connect(self.print_operation_table)

    def print_operation_table(self):
        num_rows = int(self.ui.leRows.text())
        num_columns = int(self.ui.leColumns.text())

        if self.ui.rbPlus.isChecked():
            operation = lambda x, y: x + y
        elif self.ui.rbMinus.isChecked():
            operation = lambda x, y: x - y
        elif self.ui.rbMult.isChecked():
            operation = lambda x, y: x * y
        elif self.ui.rbDiv.isChecked():
            operation = lambda x, y: x / y
        else:
            operation = lambda x, y: x * y

        table = [
            [operation(x, y) for y in range(1, num_columns + 1)]
            for x in range(1, num_rows + 1)
        ]

        table_str = ""
        for list_value in table:
            for value in list_value:
                if isinstance(value, int):
                    table_str += f"{value:4d}"
                elif isinstance(value, float):
                    table_str += f"{value:6.2f}"
            table_str += "\n"

        self.ui.lbTable.setText(table_str)


app = QtWidgets.QApplication([])
application = Task36Application()
application.show()

sys.exit(app.exec())
