"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №5
Вариант 22
"""

import csv


def serialize(filename, data, fields=None, mode='w'):
    if fields is None:
        fields = ['марка', 'модель', 'год выпуска', 'цена']
    with open(filename, mode) as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fields)
        if mode == 'w':
            writer.writeheader()
        writer.writerows(data)


def deserialize(filename):
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)


def generate_table_file(filename):
    res = [{'марка': 'Samsung', 'модель': 'Galaxy A22s', 'год выпуска': '2020', 'цена': 21999},
           {'марка': 'Huawei', 'модель': 'P30 Lite', 'год выпуска': '2019', 'цена': 9200},
           {'марка': 'Honor', 'модель': '10X Lite 4', 'год выпуска': '2019', 'цена': 15299},
           {'марка': 'Nokia', 'модель': '3310', 'год выпуска': '2000', 'цена': 4490}]
    serialize(filename, res)


def prettify_table(table):
    if isinstance(table, str):
        des = deserialize(table)
    else:
        des = table
    if not des:
        return 'Таблица пуста'
    res = [list(des[0].keys())] + list(map(lambda x: list(x.values()), des))
    maxlen = max(map(lambda x: len(max(x, key=len)), res))
    res = list(map(lambda line: "   ".join(map(lambda el: el.ljust(maxlen, " "), line)), res))
    print(*[f'{i}: {line}' for i, line in enumerate(res)], sep='\n')


def searching_by_the_model(filename):
    phones = deserialize(filename)
    models = [phone['модель'] for phone in phones]
    while not str(model := input("Введите модель:\n")) in models:
        print('Ошибка в написании модели, попробуйте снова')
    prettify_table(list(filter(lambda x: x['модель'] == model, phones)))


def sorting_by_price(filename):
    des = sorted(deserialize(filename), key=lambda phone: int(phone['цена']))
    prettify_table(des)


def adding(filename):
    fields = ['марка', 'модель', 'год выпуска', 'цена']
    data = {key: input(f'введите {key}: ') for key in fields}
    serialize(filename, [data], mode='a')
    print('Строка успешно добавлена')


def deleting(filename):
    phones = deserialize(filename)
    prettify_table(phones)
    dels = int(input('Введите номер строки, которую нужно удалить:\n')) - 1
    if dels == -1:
        print('Нельзя удалить строку с заголовками, ты чево')
        return
    elif dels > len(phones) - 1:
        print('Строки с таким номером не существует')
        return
    del phones[dels]
    serialize(filename, phones)


def main(filename):
    generate_table_file(filename)
    menu = {'1': ('Вывести имеющиеся записи', prettify_table),
            '2': ('Поиск по модели', searching_by_the_model),
            '3': ('Сортировать по цене', sorting_by_price),
            '4': ('Добавить строку', adding),
            '5': ('Удалить строку', deleting),
            '6': ('Выход из программы', exit)}

    while True:
        printable_menu = ''
        for key3, val3 in menu.items():
            printable_menu += f'{key3} - {val3[0]}\n'
        opt = input(f"Выберете опцию:\n{printable_menu}\n")
        if opt in menu.keys():
            menu[opt][1](filename)
        else:
            print('Такого варианта выбора нет\n')


if __name__ == '__main__':
    cur_file = 'p5v22.csv'
    main(cur_file)