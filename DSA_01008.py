def sinhXauNhiPhan(n,k):
    a = [0]*n
    ok = True
    def check(arr):
        return sum(arr) == k
    def inKQ(arr):
        print("".join(str(x) for x in arr))


    while ok :
        if check(a):
            inKQ(a)
        i = n-1
        while i >= 0 and a[i]==1:
            i-=1
        if i < 0 :
            ok = False
        else :
            a[i] = 1
            for j in range(i+1,n):
                a[j] = 0
t =int(input())
for _ in range(t):
    n,k =map(int,input().split())
    sinhXauNhiPhan(n,k)