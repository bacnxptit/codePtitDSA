t = int(input())
for _ in range(t):
    n = int(input())
    def backTrack(n):
        if n == 1:
            return 0
        res = float('inf')
        if n %  2 == 0 :
            res = min(res,1+backTrack(n//2))
        if n % 3 == 0:
            res =min(res,1+backTrack(n//3))
        res = min(res,1+backTrack(n-1))
        return res
    print(backTrack(n))

