def sinhXauNhiPhan(s):
    a = list(s)
    n = len(a)
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            a[i] = '0'
            for j in range(i + 1, n):
                a[j] = '1'
            return ''.join(a)
    return '1' * n

n = int(input())
for _ in range(n):
    s = ''.join(input())
    print(sinhXauNhiPhan(s))