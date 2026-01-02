def sangNT(n):
    nt = [True] * (n + 1)
    nt[0] = nt[1] = False
    p = 2
    while p * p <= n:
        if nt[p]:
            for i in range(p * p, n + 1, p):
                nt[i] = False
        p += 1
    return nt

def sumMin(n):
    nt = sangNT(n)
    for i in range(2, n):
        if nt[i] and nt[n - i]:
            return i, n - i
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    res = sumMin(n)
    if res == -1:
        print(-1)
    else:
        print(res[0], res[1])
