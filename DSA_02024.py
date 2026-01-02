n =int(input())

arr = list(map(int,input().split()))
res = []
def backTrack(index,path):
    if len(path) >= 2:
        res.append(path[:])
    for i in range(index,n):
       if not path or arr[i] > path[-1]:
           path.append(arr[i])
           backTrack(i+1,path)
           path.pop()
backTrack(0,[])
res.sort(key=lambda x: (x[0], len(x), x))
for i in res :
    print(*i)