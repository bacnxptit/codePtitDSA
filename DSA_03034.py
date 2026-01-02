def sol(a,b,c):
    i=j=k=0
    res = []
    while i < len(a) and j < len(b) and k < len(c) :
        if a[i] == b[j] == c[k] :
            res.append(a[i])
            i+= 1
            j+= 1
            k+=1
        else :
            m = min(a[i],b[j],c[k])
            if a[i] == m : i+= 1
            if b[j] == m: j += 1
            if c[k] == m: k += 1
    return res

t = int(input())
for _ in range(t):
    a,b,c = input().split()
    m = list(map(int,input().split()))
    n = list(map(int, input().split()))
    k = list(map(int, input().split()))
    if sol(m,n,k) :
        print(" ".join(map(str,sol(m,n,k))))
    else:
        print("NO")

"""
def sol(a,b,c):
    i=j=k = 0
    res = []
    while i < len(a) and j < len(b) and k < len(c) :
        if a[i[ = b[j] = c[k] :
            res.append(a[i])
            i+= 1
            j+=1 
            k+=1 
            
        else:
             m = min(a[i],b[j],c[k])
             if m == a[i] : i+= 1
             if m == b[j] : j+= 1
             if m == c[k] : k+= 1
    return res 
    
          
"""
