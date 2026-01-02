def sort(arr,n):
    for i in range(n-1):
        key_index = i
        for j in range(i+1,n):
            if arr[j] < arr[key_index]:
                key_index = j
        arr[i],arr[key_index] = arr[key_index],arr[i]
    return arr
def res(a,b,m,n):
    sort(a,n)
    sort(b,m)
    return a[n-1] * b[0]
n = int(input())
for _ in range(n):
    n , m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(res(a,b,n,m))
