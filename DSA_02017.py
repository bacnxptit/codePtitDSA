def sol(hang, total):
    global sum_max
    if hang == 8:
        sum_max = max(sum_max, total)
        return
    for i in range(8):
        if not cot[i] and not cheo1[hang - i + 7] and not cheo2[hang + i]:
            cot[i] = True
            cheo1[hang - i + 7] = True
            cheo2[hang + i] = True

            sol(hang + 1, total + board[hang][i])

            cot[i] = False
            cheo1[hang - i + 7] = False
            cheo2[hang + i] = False


t = int(input())
for _ in range(t):
    board = [list(map(int, input().split())) for __ in range(8)]

    cot = [False] * 8
    cheo1 = [False] * 15
    cheo2 = [False] * 15

    sum_max = 0
    sol(0, 0)
    print(sum_max)

"""
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
48 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64"""

