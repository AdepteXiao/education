"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №3
Вариант 22
"""
from sys import exit

alphabet_upper = 'abcdefghijklmnopqrstuvwxyz'
alphabet_lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
lis = list(''.join([alphabet_lower, alphabet_upper, numbers]))
passwords = []


def symbols_and_frequency():
    """Обшие символы и их частота"""
    upper = []
    lower = []
    num = []
    for symb in ''.join(passwords):
        if symb in alphabet_upper:
            upper.append(symb)
        elif symb in alphabet_lower:
            lower.append(symb)
        else:
            num.append(symb)
    print(f'Символы верхнего регистра: {upper}\n'
          f'Их частота: {round(len(upper) / len("".join(passwords)), 2)}\n'
          f'Символы нижнего регистра: {lower}\n'
          f'Их частота: {round(len(lower) / len("".join(passwords)), 2)}\n'
          f'Символы числа: {num}\n'
          f'Их частота: {round(len(num) / len("".join(passwords)), 2)}\n'
          )


def passw_again():
    """Новый ввод паролей"""
    while not set(passwords := ''.join(input('Введите пароли через пробел\n').split(' '))).issubset(lis):
        print('Ошибка, пароли должны содержать только латинские буквы или цифры')


def frequency_for_symbol():
    """Частота введенных символов"""
    passwords_tog = ''.join(passwords)
    while not set(sym := input('Введите символы через пробел\n').split(' ')).issubset(lis):
        print('Ошибка, символы должны быть латинскими буквами или цифрами')
    for symbo in sym:
        numm = 0
        for i in ''.join(passwords):
            if i == symbo:
                numm += 1
        print(f'Символ: {symbo}, частота: {round(numm / len(passwords_tog), 2)}')


menu = {
    '1': ('Общие символы и частота их появления', symbols_and_frequency),
    '2': ('Частота появления каждого символа', frequency_for_symbol),
    '3': ('Ввести пароли заново', passw_again),
    '4': ('Выход из программы', exit)
}
while not set(passwords := ''.join(input('Введите пароли через пробел\n').split(' '))).issubset(lis):
    print('Ошибка, пароли должны содержать только латинские буквы или цифры')
while True:
    printable_menu = ''
    for key, val in menu.items():
        printable_menu += f'{key} - {val[0]}\n'
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    if opt in menu.keys():
        print(menu[opt][1]())
    else:
        print('Такого варианта выбора нет\n')
