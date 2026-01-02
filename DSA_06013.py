def check(arr,n):
    l = len(arr)
    count = 0
    for i in arr :
        if i == n :
            count += 1
    print(count if count > 0 else -1)
n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    arr = list(map(int,input().split()))
    check(arr,b)