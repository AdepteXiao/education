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
        return expression


def polska():
    global expression
    checklist = 'abcdefghijklmnopqrstuvwxyz1234567890/+-*()'
    while not set(expression := list(input('Введите выражение без пробелов:\n'))).issubset(checklist):
        print('Выражение введено неверно, попробуйте снова')
    expression.insert(0, '!')
    expression.append('!')
    print(expression)
    numberletter = []
    usefulexp = []
    for i in expression:
        if i.isdigit() or i.isalpha():
            numberletter.append('p')
        else:
            numberletter.append(i)
    print(numberletter)
    for j in numberletter:
        if j in cipher.keys():
            usefulexp.append(cipher[j])
    print(usefulexp)
    for x in range(1, len(usefulexp)):
        i = int(usefulexp[x])
        func = variations[str(cipher[checkout[-1]])][i]
        if func.__name__ == 'one':
            func(i)
        else:
            func()
        print(checkout)


def one(i):
    checkout.append(expression[i])


def two():
    result.append(checkout[-1])
    checkout.pop()


def three():
    checkout.pop()


def four():
    print(f'Переработанный результат:\n{result}')


def five():
    print('Ошибка в написании формулы, попробуйте снова')


result = []
checkout = ['!']
expression = []
cipher = {'!': 1,
          '+': 2,
          '-': 3,
          'p': 4,
          '*': 5,
          '/': 6,
          '(': 7,
          ')': 8}
variations = {'1': (four, one, one, one, one, one, one, five),
              '2': (two, two, two, two, one, one, one, two),
              '3': (two, two, two, two, one, one, one, two),
              '4': (two, two, two, two, one, one, one, two),
              '5': (two, two, two, two, two, two, one, two),
              '6': (two, two, two, two, two, two, one, two),
              '7': (five, one, one, one, one, one, one, three)}
menu = {
    '1': ('Вывести введенное выражение', printable_expression),
    '2': ('Преобразовать в обратную польскую запись', polska),
    '3': ('Выход из программы', exit)
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
