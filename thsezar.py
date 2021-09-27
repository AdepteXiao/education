print('Введите текст, а затем сдвиг')
text = str(input())
num = int(input())
element_new = int
finished_text = ""
alphabet_upper = list('a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z')
alphabet_lower = list('A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z')

for element in text:
    if element in alphabet_upper:
        in_dex = alphabet_upper.index(element) + num
        element_new = [in_dex]
        finished_text += element_new
    elif element in alphabet_lower:
        in_dex = alphabet_lower.index(element) + num
        element_new = [in_dex]
        finished_text += element_new
    else:
        finished_text += element_new
