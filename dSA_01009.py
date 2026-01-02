def sinhxauAB(n):
    a = ['A']* n
    while True :
        print(" ".join(str(x) for x in a))
        i = n -1
        while i >= 0 and a[i] == 'B':
            i-= 1
        if i < 0 :
            break
        a[i] = 'B'
        for j in range(i+1,n):
            a[j] = 'A'

