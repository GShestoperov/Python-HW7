# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


def isRhyme(input_str: str) -> bool:
    result = True

    data_str = input_str.lower()
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

    # print(data_first)
    # print(data_second)

    return result


input_str = input("Введите стих Винни-Пуха: ")
# input_str = "пара-ра-рюм-да рам-ра-пам-папом па-ра-пе-да па-ра-пим-да"
if isRhyme(input_str):
    print("Парам пам-пам - рифма")
else:
    print("Пам парам - рифмы нет")
