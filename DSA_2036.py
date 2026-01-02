n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    res= []
    def Try(index,path,sum):
        if index == len(arr):
            if len(path)>0 and sum % 2 != 0 :
                res.append(path[:])
            return
        path.append(arr[index])
        Try(index+1,path,sum+arr[index])
        path.pop()
        Try(index+1,path,sum)
    Try(0,[],0)
    res.sort()
    for i in res :
        print(*i)
