def sol(arr,n):
    kt = None
    count = 0
    for i in arr:
        if count == 0:
            kt = i
        if i == kt :
            count += 1
        else:
            count-= 1
    if arr.count(kt) > n/2:
        return kt
    return 'No'
t = int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    print(sol(arr,n))

