def solution(n, a, b):
    jobs = [[a[i], b[i]] for i in range(n)]
    jobs.sort(key=lambda x: x[1])

    tgKt = jobs[0][1]
    count = 1

    for i in range(1, n):
        if jobs[i][0] >= tgKt:
            tgKt = jobs[i][1]
            count += 1

    return count


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    print(solution(n, a, b))
