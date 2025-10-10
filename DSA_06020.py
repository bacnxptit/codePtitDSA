def find(arr,x):
    for i in arr:
        if i == x :
            return 1
    return -1
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    print(find(arr,x))