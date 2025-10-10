def partition(arr, l, r):
    pivot = arr[r][0]
    i = l - 1
    for j in range(l, r):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quickSort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quickSort(arr, l, pivot - 1)
        quickSort(arr, pivot + 1, r)

def tinhGTTuyetDoi(arr, k):
    res = [(abs(x - k), x) for x in arr]

    quickSort(res, 0, len(res) - 1)

    sortRes = [item[1] for item in res]
    return sortRes


n = int(input())
for _ in range(n):
    x, k = map(int, input().split())
    A = list(map(int, input().split()))
    b = tinhGTTuyetDoi(A, k)
    print(" ".join(map(str, b)))
