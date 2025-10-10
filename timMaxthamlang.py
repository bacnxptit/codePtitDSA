def timTongMax(arr):
    arr.sort()
    max = 0
    mod  = 10 ** 9 + 7
    for i in range(0,len(arr)):
        tich = i * arr[i]
        tich %= mod
        max+=tich
        max %= mod
    return max
n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int,input().split()))
    print(timTongMax(arr))
