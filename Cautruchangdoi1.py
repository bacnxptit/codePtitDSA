t = int(input())
for _ in range(t):
    n = int(input())
    q = []
    for _ in range(n):
        ptu = input().split()
        dk = int(ptu[0])

        if dk == 1:
            print(len(q))

        elif dk == 2:
            if len(q)==0:
                print('YES')
            else:
                print('NO')

        elif dk == 3:
            x = int(ptu[1])
            q.append(x)

        elif dk == 4:
            if len(q) > 0:
                q.pop(0)

        elif dk == 5:
            if len(q) > 0 :
                print(q[0])
            else:
                print(-1)

        elif dk == 6:
             if len(q) > 0:
                 print(q[-1])
             else:
                 print(-1)
