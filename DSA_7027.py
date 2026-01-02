n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    res = []

    for i in range(k):
        found = False
        for j in range(i+1, k):
            if arr[j] > arr[i]:
                res.append(arr[j])
                found = True
                break
        if not found:
            res.append(-1)
    print(*res)

