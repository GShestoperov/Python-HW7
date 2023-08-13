#  Сделайте локальный чат-бот с внешним хранилищем. Тема чат-бота - любая вам интересная.

from random import *
import json

films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")


def load():
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена")


try:
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена")
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара")


while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
        with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека была успешно загружена")
    elif command == "/stop":
        save()
        print("Бот остановил свою работа. Заходите еще!")
        break
    elif command == "/all":
        print("Вот текущий список фильмов: ")
        print(films)
    elif command == "/add":
        f = input("Введите название фильма: ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command == "/help":
        print("Здесь какой-то мануал!")
    elif command == "/delete":
        f = input("Введите название фильма: ")
        try:
            films.remove(f)
            print("Фильм был успешно удален!")
        except:
            print("Фильм не найден ")
    elif command == "/random":
        print("Случайный фильм - " + choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека была успешно загружена")
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")
