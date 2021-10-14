"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №2
Вариант 22
"""

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
    avgm = []
    for student, subjects in STUDENTS.items():
        marks = [mark for subj, mark in subjects.items()]
        avgm.append((student, round(sum(marks) / len(marks), 2)))
    avgm = '\n'.join(list(map(lambda x: f'{x[0]} - {str(x[1])}', avgm)))
    return avgm


def average_value():
    global SUBJ, STUDENTS
    vals = {sub: [] for sub in SUBJ}
    for stud, subj in STUDENTS.items():

    print(vals)


subjlist = list(STUDENTS[list(STUDENTS.keys())[0]].keys())
while not set(SUBJ := input('Введите предметы через пробел\n').split(' ')).issubset(subjlist):
    print('Какой-то из предметов неверно написан либо не существует')

average_value()
# print('')
# text = 'meh'
# while text != 'нет':
#     print('Введите "да", чтобы начать, или "нет", чтобы завершить программу')
#     if (text := input()) == 'да':
#         just_run_it_already()
#     elif text == 'нет':
#         print('Программа завершена')
#     else:
#         print('Ошибка')
# print(avg_4_students())
