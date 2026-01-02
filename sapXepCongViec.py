def sapXepCV(n, a, b):
    jobs = [(a[i], b[i]) for i in range(n)]
    jobs.sort(key=lambda x: x[1])
    chonCV = [jobs[0]]
    thoiGianKT = jobs[0][1]
    for i in range(1, n):
        if jobs[i][0] >= thoiGianKT:
            chonCV.append(jobs[i])
            thoiGianKT = jobs[i][1]

    return chonCV


t = int(input())
for _ in range(t):
    k = int(input())
    a, b = [], []
    for _ in range(k):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(len(sapXepCV(k,a,b)))


