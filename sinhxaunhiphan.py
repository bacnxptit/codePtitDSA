def kiemTraDoiXung(s):
    return s == s[::-1]
def sinhXaunhiPhan(n):
    a  = ['0'] * n
    while True :
        if kiemTraDoiXung(" ".join(a)):
            print(" ".join(a))
        i = n-1
        while i >= 0 and a[i] == '1' :
            i-= 1
        if i < 0 :
            break
        a[i] = '1'
        for j in range(i+1,n):
            a[j] = '0'
    return a
sinhXaunhiPhan(int(input()))


