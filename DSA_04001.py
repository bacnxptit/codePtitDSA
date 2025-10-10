def tinhLuyThua(n, k):
    mod = 10**9 + 7
    if k == 0:
        return 1
    half = tinhLuyThua(n, k // 2) % mod   
    if k % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * n) % mod
t =int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(tinhLuyThua(n,k))