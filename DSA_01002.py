def sinhToHop(n,k,a):
    i = k - 1
    while i > 0 and a[i] == n - k + i + 1 :
        i -= 1
    if i < 0 :
        return list(range(1,k+1))
    a[i] += 1
    for j in range(i + 1, k):
        a[j] = a[j - 1] + 1
    return a
t  =int(input())
for _ in range(t):
    n ,k = map(int,input().split())
    x = list(map(int,input().split()))
    print(' '.join(map(str,sinhToHop(n,k,x))))

