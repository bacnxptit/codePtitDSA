def check(arr):
    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
            return 0
    return 1
n = int(input())
for _ in range(n):
    k =int(input())
    arr = list(map(int,input().split()))
    print(check(arr))