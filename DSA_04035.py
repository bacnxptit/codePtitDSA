def tinhLuyThua(n, k):
    mod = 10**9 + 7
    if k == 0:
        return 1
    half = tinhLuyThua(n, k // 2) % mod
    if k % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * n) % mod
while True:
    n , k = map(int,input().split())
    if n == k == 0:
        break
    print(tinhLuyThua(n,k))