def sinhxaunhiphan(n):
    a = [0]*n
    while True :
        print("".join(str(x) for x in a ))
        i = n-1
        while i >= 0 and a[i] == 1:
            i-= 1
        if i < 0 :
            break
        a[i]=1
        for j in range(i+1,n):
            a[j]=0
    return a
print(sinhxaunhiphan(3))