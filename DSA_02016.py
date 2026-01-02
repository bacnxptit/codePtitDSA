
def sol(hang):
    if hang == n:
        return 1
    count = 0
    for i in range(n):
        if cot[i] and cheo1[hang - i + n - 1] and cheo2[hang + i]:
            cot[i] = cheo1[hang - i + n - 1] = cheo2[hang + i] = False
            count += sol(hang + 1)
            cot[i] = cheo1[hang - i + n - 1] = cheo2[hang + i] = True
    return count
t = int(input())
for _ in range(t):
    n = int(input())
    cot = [True] * n
    cheo1 = [True] * (2*n - 1)
    cheo2 = [True] * (2*n - 1)
    print(sol(0))
