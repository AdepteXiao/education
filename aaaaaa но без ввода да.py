num = int(input())
co_num = list(range(1, num + 1))
lent = len(co_num)
for i in range(1, num + 1):
    co_num = list(range(1, i + 1))
    co_num = co_num[::-1]
    print((' ' * lent) * 2, *co_num)
for i in range(num, 0, -1):
    co_num = list(range(1, i + 1))
    print((' ' * (lent - i)) * 2, *co_num)
