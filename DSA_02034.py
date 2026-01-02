def sol(n):
    use = [False]* (n+1)
    path = []
    def backTracking():
        if len(path) == n :
            print("".join(map(str,path)))
        for i in range(1,n+1):
            if not use[i]:
                if path and abs(i - path[-1]) == 1:
                    continue
                use[i] = True
                path.append(i)
                backTracking()
                path.pop()
                use[i] = False
    backTracking()
t  = int(input())
for i in range(t):
    n = int(input())
    sol(n)


