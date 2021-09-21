"""
КИ21 - 17/1b Демёхина Арина Руслановна
ОП Лабораторная №1
Вариант 22
"""


def just_run_it_already():
    """Функция - ввод и проверка чисел на факт существования в множестве чисел нивена"""
    while not (number := input('Введите положительное натуральное число для проверки:')).isdigit():
        print('Ошибка, некорректные входные данные')
    number = int(number)
    if number == 0:
        print('Число не является числом нивена')
        print('Число не является множественным числом нивена')
    else:
        first = number
        first_sum_num = 0
        second_sum_num = 0
        while first > 0:
            first_sum_num += first % 10
            first //= 10
        if number % first_sum_num == 0:
            print('Число является числом нивена')
            second = number // first_sum_num
            while second > 0:
                second_sum_num += second % 10
                second //= 10
            if (number // first_sum_num) % second_sum_num == 0:
                print('Число является множественным числом нивена')
            else:
                print('Число не является множественным числом нивена')
        else:
            print('Число не является числом нивена')
            print('Число не является множественным числом нивена')


print('Числа Нивена — натуральные числа, делящиеся нацело на сумму своих цифр.')
text = 'meh'
while text != 'нет':
    print('Введите "да", чтобы проверить число, или "нет", чтобы завершить программу')
    if (text := input()) == 'да':
        just_run_it_already()
    elif text == 'нет':
        print('Программа завершена')
    else:
        print('Ошибка')
