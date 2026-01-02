n = int(input())
def isPrime(n):
    if n  < 2 :
        return False
    for  i in range(2,int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True

for _ in range(n):
    k = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    res= []
    def Try(index,path,sum):
        if index == len(arr):
            if len(path)>0 and isPrime(sum) :
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
