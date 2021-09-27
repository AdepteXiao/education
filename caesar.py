def get_el(arr, ind):
    a = ind % len(arr)
    return arr[a]


def caesar():
    print('Введите текст, а затем сдвиг')
    text = input()
    shift = int(input())
    alphabet_upper = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_lower = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    cipher = []
    for i in text:
        if i in alphabet_lower:
            cipher.append(get_el(alphabet_lower, alphabet_lower.index(i) + shift))
        elif i in alphabet_upper:
            cipher.append(get_el(alphabet_upper, alphabet_upper.index(i) + shift))
        else:
            cipher.append(i)
    return ''.join(cipher)


z = 'meh'
while z != 'нет':
    print('Введите "да", чтобы начать, или "нет", чтобы завершить программу')
    if (z := input()) == 'да':
        print(caesar())
    elif z == 'нет':
        print('Программа завершена')
    else:
        print('Ошибка')
