def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        key = i
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                key = j
        arr[key],arr[i] = arr[i],arr[key]
    return arr
def tinh(arr):
    selectionSort(arr)
    n = len(arr)
    return arr[n-1] + arr[n-2]
k = int(input())
for _ in range(k):
    n = int(input())
    arr = list(map(int,input().split()))
    print(tinh(arr))