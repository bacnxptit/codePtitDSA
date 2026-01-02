def solve(arr,k):
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == k:
                count+= 1
    return count
t =int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(arr,k))

