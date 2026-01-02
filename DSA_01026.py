def check(s):
    if '88' in s :
        return False
    if '6666' in s :
        return False
    return True
def sinhSo68(n):
    if n < 6 :
        return
    a = ['6'] * n
    a[0] = '8'
    a[-1]= '6'

    def kiemTra():
        s = "".join(a)
        if check(s) :
            print(s)
    kiemTra()

    while True :
        i = n -2
        while i >0 and a[i] == '8' :
            a[i] = '6'
            i-=1
        if i == 0 :
            break
        a[i] = '8'
        kiemTra()
n = int(input())
sinhSo68(n)


