n = int(input())
for _ in range(n):
    s  = input().strip()
    stack = []
    for i in s :
        if i.isalnum():
            stack.append(i)
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            new = f"({s2}{i}{s1})"
            stack.append(new)
    print("".join(stack))