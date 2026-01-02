n = int(input())
for _ in range(n):
    s  = input().strip()
    stack = []
    dauNgoac = {
        '(':')',
        '[':']',
        '{':'}'
    }
    ok = True

    for i in s :
        if i in dauNgoac.keys():
            stack.append(i)
        elif i in dauNgoac.values():
            if not stack:
                ok = False
                break
            check = stack.pop()
            if dauNgoac[check] != i:
                ok = False
                break
    if ok and not stack:
        print("YES")
    else:
        print("NO")
