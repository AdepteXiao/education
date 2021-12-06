"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №4
Вариант 22
"""
from sys import exit


def printable_expression():
    if expression == '':
        print('Вы ещё не ввели никакое выражение')
    else:
        print(expression)


def input_expression():
    z = 0
    while z != 1:
        global expression
        expression = list(input('Введите выражение без пробелов:\n'))
        for i in expression:
            if i not in checklist:
                print(f'Выражение введено неверно, символа {i} быть не должно')
                break
        z += 1


def one(i):
    checkout.append(i)


def two():
    result.append(checkout[-1])
    checkout.pop()


def three():
    checkout.pop()


def four():
    print(f'Переработанный результат:\n{result}')


def five():
    print('Ошибка в написании формулы, попробуйте снова')


def polska():
    expression.append('!')
    for i in range(1, len(expression)):
        if expression[i] == '!':
            variations[expression[i-1]][0]()
        elif expression[i] == '+':
            variations[expression[i-1]][1]()
        elif expression[i].isdigit() or expression[i].isalpha():
            if expression[expression[i-1]].isdigit or expression[expression[i-1]].isalpha:
                variations['p'][2]()
            else:
                variations[expression[i-1]][2]()
        elif expression[i] == '*':
            variations[expression[i-1]][3]()
        elif expression[i] == '/':
            variations[expression[i-1]][4]()
        elif expression[i] == '(':
            variations[expression[i-1]][5]()
        elif expression[i] == ')':
            variations[expression[i-1]][6]()


checkout = ['!']
checklist = 'abcdefghijklmnopqrstuvwxyz1234567890/+-*()'
result = []
expression = []
variations = {'!': (four, one, one, one, one, one, five),
              '+': (two, two, two, one, one, one, two),
              '-': (two, two, two, one, one, one, two),
              'p': (two, two, two, one, one, one, two),
              '*': (two, two, two, two, two, one, two),
              '/': (two, two, two, two, two, one, two),
              '(': (five, one, one, one, one, one, three)}
menu = {
    '1': ('Вывести введенное выражение', printable_expression),
    '2': ('Ввести выражение', input_expression),
    '3': ('Преобразовать в обратную польскую запись', polska),
    '4': ('Выход из программы', exit)
}
while True:
    printable_menu = ''
    for key3, val3 in menu.items():
        printable_menu += f'{key3} - {val3[0]}\n'
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    if opt in menu.keys():
        print(menu[opt][1]())
    else:
        print('Такого варианта выбора нет\n')
