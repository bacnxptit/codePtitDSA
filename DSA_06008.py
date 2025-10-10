def demSoCap(a,b):
    count = 0
    for x in a:
        for y in b :
            if pow(x,y) >pow(y,x):
                count +=1
    return count
t =int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(demSoCap(a, b))
