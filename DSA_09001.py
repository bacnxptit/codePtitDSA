def solve():
    import sys
    data = sys.stdin.read().strip().split()
    it = iter(data)

    T = int(next(it))
    for _ in range(T):
        V = int(next(it))
        E = int(next(it))

        adj = [[] for _ in range(V + 1)]

        for _ in range(E):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)

        for i in range(1, V + 1):
            adj[i].sort()
            print(i, end=": ")
            for x in adj[i]:
                print(x, end=" ")
            print()
solve()