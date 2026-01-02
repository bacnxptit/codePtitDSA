def sort(arr,k):
    n = len(arr)
    for i in range(n):
        for j in range (n-i-1):
            if arr[j+1]< arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    res = []
    for i in range(n-1,n-k-1,-1):
        res.append(arr[i])
    return res

n = int(input())
for _ in range(n):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(" ".join(map(str,sort(arr,k))))




