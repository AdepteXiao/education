from math import log2


def rep_ins_arr(arr, start, i_arr):
    return arr[:start - 1] + i_arr + arr[start:]


def tab_1(f_name):
    with open(f_name, 'r', encoding='utf-8') as file:
        _n = file.readlines()
    _n = filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), _n))
    _n = list(map(lambda x: x.split('\t') if '-' in x else x, _n))
    n = []
    for i in _n:
        if isinstance(i, str):
            n.append(i)
        else:
            n.extend(i)

    res = []
    for i in range(0, len(n), 10):
        res.append((n[i], n[i + 1: i + 10]))
    res = [(i[0], tuple(map(lambda x: x.replace(',', '.').replace(' ', ''), i[1]))) for i in res]
    res = list(map(lambda x: (
        int(x[0]), tuple(filter(lambda x: x != '', map(lambda y: float(y) if '-' not in y else '', x[1])))), res))
    return res


def tab_23(f_name):
    with open(f_name, 'r') as file:
        n = file.readlines()
    n = list(map(float, filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), n))))
    res = []
    for i in range(0, len(n), 2):
        res.append((n[i], n[i + 1]))
    res = sorted(list(map(lambda x: (int(x[0]), x[1]) if x[0] >= 1 else x, res)), key=lambda x: x[0])
    resv2 = {}
    for key, item in res:
        resv2[key] = item
    return resv2


def tab_4(f_name):
    with open(f_name, 'r', encoding='utf-8') as file:
        n = file.readlines()
    n = list(filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), n)))
    res = []
    for i in n:
        if not set(i).issubset(set('1234567890.')):
            res.append([i])
        else:
            for c, j in enumerate(res):
                if len(j) == 1:
                    res[c].append(i)
                    break

    return list(map(tuple, res))


TAB1 = tab_1('tab1.txt')
TAB2 = tab_23('tab2.txt')
TAB3 = tab_23('tab3.txt')
TAB4 = tab_4('tab4.txt')


def h(p):
    return TAB2.get(p, -round(p * log2(p), 2))


def l(n):
    return TAB3.get(n, round(log2(n), 2))


def do_task(var=None):
    if isinstance(var, int):
        var, alph = TAB1[var - 1]
        print(f'Вариант {var}, вероятности символов: {", ".join(map(str, alph))}')
    else:
        print(f'Задание 2, русский алфавит, вероятности символов:\n{", ".join([i[1] for i in TAB4])}')
        alph = [float(i[1]) for i in TAB4]

    print('Вычислим среднюю энтропию:')
    for p in alph:
        print(f' - {p}log₂({p})', end='')
    print('=')
    s = 0
    for z, p in enumerate(alph):
        x = h(p)
        if z != len(alph) - 1:
            print(f'{x} + ', end='')
        else:
            print(f'{x} ', end='')
        s += x
    s = round(s, 2)
    print('=', s)
    print('Избыточность:')
    print(f'Hmax = log₂({len(alph)}) = {l(len(alph))}')
    hmax = l(len(alph))
    d = ((hmax - s) / hmax) * 100

    print(f'D = (({hmax} - {s}) / {hmax}) * 100% = {round(d, 2)}%')


do_task(1)
print()
do_task()

