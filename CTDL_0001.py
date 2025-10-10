def doiXung(s):
    return s == s[::-1]
def sinhXauNhiPhan(n):

    s = ['0'] * n
    while True:
        if doiXung(''.join(s)):
            print(' '.join(s))
        i = n - 1
        while i >= 0 and s[i] == '1':
            i -= 1
        if i < 0:
            break
        s[i] = '1'
        for j in range(i + 1, n):
            s[j] = '0'

n = int(input())
sinhXauNhiPhan(n)
