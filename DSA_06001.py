def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quickSort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quickSort(arr, l, pivot - 1)
        quickSort(arr, pivot + 1, r)
def sapXepXenKe(arr):
    quickSort(arr,0,len(arr)-1)
    left ,right = 0,len(arr)-1
    res = []
    while left <= right :
        res.append(arr[right])
        right -= 1
        if left <= right :
            res.append(arr[left])
            left += 1
    return res
n = int(input())
for _ in range (n):
    x = int(input())
    A = list (map(int,input().split()))
    print(*sapXepXenKe(A))

