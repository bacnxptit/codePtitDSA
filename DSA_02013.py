def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def Try(pos, total, cnt, path):
    if cnt == N:
        if total == S:
            res.append(path[:])
        return
    for i in range(pos, len(prime)):
        if total + prime[i] > S:
            break
        path.append(prime[i])
        Try(i + 1, total + prime[i], cnt + 1, path)
        path.pop()

t = int(input())
for _ in range(t):
    N, P, S = map(int, input().split())
    prime = [x for x in range(P+1, S) if isPrime(x)]
    res = []
    Try(0, 0, 0, [])
    print(len(res))
    for i in res:
        print(*i)
