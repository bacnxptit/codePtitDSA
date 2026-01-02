def tinh(arr):
    arr.sort()
    n= len(arr)
    tich1 = arr[n-1]*arr[n-2]
    tich2 = arr[n-1]*arr[n-2]*arr[n-3]
    tich3 = arr[0]*arr[1]*arr[n-1]
    return max(tich1,tich2,tich3)
n = int(input())
arr = list(map(int,input().split()))
print(tinh(arr))
