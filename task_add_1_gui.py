# Задание 1 необязательное Сделайте локальный чат-бот с внешним хранилищем. Тема чат-бота - любая вам интересная.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from task_add_1_ui import Ui_MainWindow
from random import *
import json


class Task_add_1_Application(QtWidgets.QMainWindow):
    films = []

    def save(self):
        with open("films.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(self.films, ensure_ascii=False))
        self.add_str("Наша фильмотека была успешно сохранена в файле films.json")

    def load(self):
        with open("films.json", "r", encoding="utf-8") as fh:
            self.films = json.load(fh)
        self.add_str("Фильмотека была успешно загружена")

    def __init__(self):
        super(Task_add_1_Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        try:
            self.load()
        except:
            self.films.append("Матрица")
            self.films.append("Солярис")
            self.films.append("Властелин колец")
            self.films.append("Техасская резня бензопилой")
            self.films.append("Санта Барбара")

    def init_UI(self):
        self.ui.btCommand.clicked.connect(self.CommandClick)

    def add_str(self, data_str):
        self.ui.pteData.appendPlainText(data_str)

    def CommandClick(self):
        command_str = self.ui.leCommand.text()
        self.add_str(command_str)
        self.bot(command_str)
        self.ui.leCommand.setText("")

    # признак ожидания ввода внутри команды
    into_command = False
    command_name = ""

    def bot(self, command):
        if self.into_command:
            if self.command_name == "/add":
                f = command
                self.films.append(f)
                self.add_str("Фильм был успешно добавлен в коллекцию!")
            elif self.command_name == "/delete":
                f = command
                try:
                    self.films.remove(f)
                    self.add_str("Фильм был успешно удален!")
                except:
                    self.add_str("Фильм не найден ")
            self.ui.label.setText("Введите команду: ")
            self.into_command = False
            return

        if command == "/start":
            self.add_str("Бот-фильмотека начал свою работу")
            self.load()
        elif command == "/stop":
            self.save()
            self.add_str("Бот остановил свою работа. Заходите еще!")
            exit()
        elif command == "/all":
            self.add_str("Вот текущий список фильмов: ")
            self.add_str(str(self.films))
        elif command == "/add":
            self.into_command = True
            self.command_name = "/add"
            self.add_str("Введите название фильма: ")
            self.ui.label.setText("Введите название фильма: ")
        elif command == "/help":
            self.add_str("Здесь какой-то мануал!")
        elif command == "/delete":
            self.into_command = True
            self.command_name = "/delete"
            self.add_str("Введите название фильма: ")
            self.ui.label.setText("Введите название фильма: ")
        elif command == "/random":
            self.add_str("Случайный фильм - " + choice(self.films))
        elif command == "/save":
            self.save()
        elif command == "/load":
            self.load()
        else:
            self.add_str("Неопознанная команда. Просьба изучить мануал через /help")


app = QtWidgets.QApplication([])
application = Task_add_1_Application()
application.show()

sys.exit(app.exec())
