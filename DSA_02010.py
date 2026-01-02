t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = []

    def Try(index, path, total):
        if total == x:
            res.append(path[:])
            return
        if total > x:
            return
        for i in range(index, n):
            path.append(arr[i])
            Try(i, path, total + arr[i])
            path.pop()

    Try(0, [], 0)

    if res:
        for i in res:
            print(f"[{' '.join(map(str, i))}]", end=" ")
        print()

    else:
        print(-1)
