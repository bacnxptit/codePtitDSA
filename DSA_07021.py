n = int(input())
for _ in range(n):
    s = input().strip()
    stack = [-1]
    lonNhat = 0
    for i ,ch in enumerate(s) :
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack :
                stack.append(i)
            else:
                lonNhat = max(lonNhat, i - stack[-1])
    print(lonNhat)

            