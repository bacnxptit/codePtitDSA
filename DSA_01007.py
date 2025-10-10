def inKQ(a,n):
    s = "".join("A" if a[i] == 0 else "B" for i in range(n))
    print(s,end=" ")
def sinhXauNhiPhan(n):
    a = [0]*n
    ok = True
    while ok :
        inKQ(a,n)
        i = n-1
        while i >= 0 and a[i] == 1:
            i-=1
        if i < 0 :
            ok = False
        else :
            a[i] = 1
            for j in range(i+1,n):
                a[j] = 0
t = int(input())
for _ in range(t):
    n = int(input())
    sinhXauNhiPhan(n)
    print()
