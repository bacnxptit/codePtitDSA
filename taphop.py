def count_sets(n, k, s):
    res = 0
    def backtrack(start, count, total):
        nonlocal res

        if count == k:
            if total == s:
                res += 1
            return
        if total > s or start > n:
            return

        for i in range(start, n + 1):
            backtrack(i + 1, count + 1, total + i)

    backtrack(1, 0, 0)
    return res

while True:
    n, k, s = map(int, input().split())
    if n == 0 and k == 0 and s == 0:
        break
    print(count_sets(n, k, s))
