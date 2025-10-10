def xauAB(a,n):
    s = "".join("A" if a[i]=='0' else "B" for i in range(n))
    print(s,end = " ")
def sinhXaunhiPhan(n):
    a  = ['0'] * n
    while True :
        xauAB(a,n)
        i = n-1
        while i >= 0 and a[i] == '1' :
            i-= 1
        if i < 0 :
            break
        a[i] = '1'
        for j in range(i+1,n):
            a[j] = '0'
    return a
t  = int(input())
for _ in range(t):
    k = int(input())
    sinhXaunhiPhan(k)
    print()









