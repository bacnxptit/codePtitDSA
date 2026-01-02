def tong_max(a, n):
    tong_ht = a[0]
    tong_max = a[0]
    for i in range(1, n):
        tong_ht = max(a[i], tong_ht + a[i])
        tong_max = max(tong_max, tong_ht)
    return tong_max

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(tong_max(a, n))
