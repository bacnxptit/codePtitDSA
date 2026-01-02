n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    check_du = False
    for c in s:
        if c == ')':
            check_dau = False
            while stack and stack[-1] != '(':
                top = stack.pop()
                if top in "+-*/":
                    check_dau = True
            if stack:
                stack.pop()
            if not check_dau:
                check_du = True
                break
        else:
            stack.append(c)

    if check_du:
        print("Yes")
    else:
        print("No")
