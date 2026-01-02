def sol(n):
    res = []
    path = []
    def backtrack():
        if 1 <= len(path) <= n :
            res.append(int("".join(map(str,path[:]))))
        if len(path) == n :
            return

        path.append('6')
        backtrack()
        path.pop()

        path.append('8')
        backtrack()
        path.pop()
    backtrack()
    res.sort(reverse=True)
    print(len(res))
    for i in res :
        print(i,end=" ")
n =int(input())
for _ in range(n):
    k =int(input())
    sol(k)
    print()
