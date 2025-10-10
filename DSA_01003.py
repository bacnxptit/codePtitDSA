def sinhHoanViKeTiep(a):
    l = len(a)
    i=l-2
    while i > 0 and a[i] >= a[i+1]:
        i-= 1
    if i == - 1 :
        a.reverse()
        return a
    j = l-1
    while a[j] <= a[i]:
        j-= 1
    a[j],a[i] = a[i],a[j]
    a[i+1:] = reversed(a[i+1:])
    return a
t =int(input())
for _ in range(t):
    n = int(input())
    x= list(map(int,input().split()))
    print(" ".join(map(str, sinhHoanViKeTiep(x))))
