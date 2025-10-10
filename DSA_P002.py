def sinhHoanVi(a):
    l = len(a)
    i = l -2
    while i >=0 and a[i] > a[i+1]:
        i-= 1
    if i < 0 :
        return False
    j = l -1
    while j >= 0 and a[j] < a[i]:
        j-= 1
    a[j],a[i] = a[i],a[j]
    left = i +1
    right  = l-1
    while left  < right :
        a[left],a[right]=a[right],a[left]
        left += 1
        right -= 1
    return True
def inHoanVi(n):
    a = list(range(1, n+1))
    cnt = 1
    print(f"{cnt}: {' '.join(map(str, a))}")
    while sinhHoanVi(a):
        cnt += 1
        print(f"{cnt}: {' '.join(map(str, a))}")

n=int(input())
inHoanVi(n)
