n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    res = []
    def sol(index,path,sum):
        if sum == b :
            res.append(path[:])
            return
        for i in range(index,a):
            path.append(arr[i])
            sol(i +1 ,path,sum+arr[i])
            path.pop()
    sol(0,[],0)
    if res :
        for i in res :
            print("["+" ".join(map(str,i))+"]",end=" ")
        print()
    else:
        print(-1)
