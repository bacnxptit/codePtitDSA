def timKiemThuK(arr,n,k):

    l = 0
    r = n -1
    mid = (l+r)//2
    while l <= r :
        if k < arr[mid]:
            r = mid -1
        elif k > arr[mid]:
            l = mid + 1
        else:
            return mid + 1
        mid = (l+r)//2
    return "NO"
k =int(input())
for _ in range(k):
    x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    print(timKiemThuK(arr,x,y))
