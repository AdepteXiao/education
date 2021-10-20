"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №2
Вариант 22
"""
from sys import exit

STUDENTS = {'Chongyun': {'Adepte-knowlege': 4,
                         'Economy': 4,
                         'History': 6,
                         'Maths': 6,
                         'Stone-science': 3},
            'Ganyu': {'Adepte-knowlege': 8,
                      'Economy': 10,
                      'History': 1,
                      'Maths': 8,
                      'Stone-science': 6},
            'Hu Tao': {'Adepte-knowlege': 5,
                       'Economy': 3,
                       'History': 3,
                       'Maths': 3,
                       'Stone-science': 6},
            'Keqing': {'Adepte-knowlege': 10,
                       'Economy': 10,
                       'History': 10,
                       'Maths': 10,
                       'Stone-science': 10},
            'Ningguang': {'Adepte-knowlege': 1,
                          'Economy': 10,
                          'History': 7,
                          'Maths': 10,
                          'Stone-science': 9},
            'Xiangling': {'Adepte-knowlege': 6,
                          'Economy': 5,
                          'History': 3,
                          'Maths': 1,
                          'Stone-science': 7},
            'Xiao': {'Adepte-knowlege': 8,
                     'Economy': 5,
                     'History': 1,
                     'Maths': 7,
                     'Stone-science': 6},
            'Xinqiu': {'Adepte-knowlege': 10,
                       'Economy': 1,
                       'History': 10,
                       'Maths': 6,
                       'Stone-science': 1},
            'Xinyan': {'Adepte-knowlege': 1,
                       'Economy': 3,
                       'History': 4,
                       'Maths': 3,
                       'Stone-science': 3},
            'Zhongli': {'Adepte-knowlege': 10,
                        'Economy': 1,
                        'History': 10,
                        'Maths': 9,
                        'Stone-science': 10}}


def avg_4_students():
    """Функция высчитывает и выводит среднее значение для всех студентов"""
    avgm = []
    for student, subjects in STUDENTS.items():
        marks = [mark for subj, mark in subjects.items()]
        avgm.append((student, round(sum(marks) / len(marks), 2)))
    avgm = '\n'.join(list(map(lambda x: f'{x[0]} - {str(x[1])}', avgm)))
    return avgm


def average_value():
    """Функция высчитывает и выводит среднее значение по предметам"""
    global SUBJ, STUDENTS
    res = {sub: [] for sub in SUBJ}
    for stud, subj in STUDENTS.items():
        for sub, val in subj.items():
            if sub in res.keys():
                res[sub].append(val)
    for sub in res.keys():
        res[sub] = round(sum(res[sub]) / len(res[sub]), 2)
    ress = ''
    for key, val in res.items():
        ress += f'{key} - {val}\n'
    return ress


def printable_marks():
    """Функция выводит всех студентов и их оценки по предметам"""
    global STUDENTS
    res = ''
    for stud, marks in STUDENTS.items():
        res += f'Оценки {stud}:\n'
        for sub, val2 in marks.items():
            res += f'{val} по {sub}\n'
        res += '\n'
    return res


subjlist = list(STUDENTS[list(STUDENTS.keys())[0]].keys())
while not set(SUBJ := input('Введите предметы через пробел\n').split(' ')).issubset(subjlist):
    print('Какой-то из предметов неверно написан либо не существует')
menu = {
    '1': ('Вывести все данные', printable_marks),
    '2': ('Средние оценки по выбранному предмету', average_value),
    '3': ('Средние оценки для всех студентов', avg_4_students),
    '4': ('Выход из программы', exit)
}
while True:
    printable_menu = ''
    for key3, val3 in menu.items():
        printable_menu += f'{key3} - {val3[0]}\n'
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    if opt in menu.keys():
        print(menu[opt[1]]())
    else:
        print('Такого варианта выбора нет\n')
