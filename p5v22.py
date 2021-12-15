"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №5
Вариант 22
"""


import csv
import operator
from sys import exit


with open("p5v22.csv", "w", newline='') as file:
    fields = ['марка', 'модель', 'год выпуска', 'цена']
    writer = csv.DictWriter(file, delimiter=';', fieldnames=fields)
    writer.writeheader()
    writer.writerow({'марка': 'Samsung', 'модель': 'Galaxy A22s', 'год выпуска': '2020', 'цена': '21999'})
    writer.writerow({'марка': 'Huawey', 'модель': 'P30 Lite', 'год выпуска': '2019', 'цена': '9200'})
    writer.writerow({'марка': 'Honor', 'модель': '10X Lite 4', 'год выпуска': '2019', 'цена': '15299'})
    writer.writerow({'марка': 'Nokia', 'модель': '3310', 'год выпуска': '2000', 'цена': '4490'})
models = ['Galaxy A22s',  'P30 Lite', '10X Lite 4', '3310']


def reading_whole_file():
    with open('p5v22.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for i, line in enumerate(reader):
            if i == 0:
                print(f'{i}: {" ".join(line)}')
            else:
                print(f'{i}: {" ".join([" " * (15 - len(s)) + s for s in line])}')


def searching_by_the_model():
    while not str(model := input("Введите модель:\n")) in models:
        print('Ошибка в написании модели, попробуйте снова')
    with open('p5v22.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for line in enumerate(reader):
            if line[2] == model:
                print(" ".join(line))
        f.close()


def sorting_by_price():
    with open('p5v22.csv', 'rb') as f:
        data = csv.reader(open('p5v22.csv'), delimiter=',')
        sortedlist = sorted(data, key=operator.itemgetter(3), reverse=True)
        for item in sortedlist:
            print(item)
        f.close()


def adding():
    data = dict()
    for i in fields:
        key = i
        value = input(f'введите {key}: ')
        data[key] = value
    with open('p5v22.csv', 'a', newline='') as f:
        wri = csv.DictWriter(file, delimiter=';', fieldnames=fields)
        writer.writeheader()
        wri.writerow(data)
        f.close()


def deleting():
    lis = list(input("Введите марку, модель, год выпуска и цену через пробел"))
    with open('p5v22.csv', 'a', newline='') as f:
        wri = csv.writer(f)
        wri.writerow(lis)
        f.close()


menu = {
    '1': ('Вывести имеющиеся записи', reading_whole_file),
    '2': ('Поиск по модели', searching_by_the_model),
    '3': ('Сортировать по цене', sorting_by_price),
    '4': ('Добавить строку', adding),
    '5': ('Удалить строку', deleting),
    '7': ('Выход из программы', exit)}
while True:
    printable_menu = ''
    for key3, val3 in menu.items():
        printable_menu += f'{key3} - {val3[0]}\n'
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    if opt in menu.keys():
        print(menu[opt][1]())
    else:
        print('Такого варианта выбора нет\n')
