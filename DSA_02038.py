n = int(input())
for _ in range(n):
    n , k = map(int,input().split())
    arr= list(map(int,input().split()))
    arr.sort()
    res = []
    def Try(index,path):
        if len(path) == k :
            res.append(path[:])
            return
        for i in range(index,n):
            path.append(arr[i])
            Try(i+1,path)
            path.pop()
    Try(0,[])
    for i in res:
        print(*i)
