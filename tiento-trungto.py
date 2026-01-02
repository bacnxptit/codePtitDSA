n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    for i in s[::-1]:
        if i.isalnum():
            stack.append(i)
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            bT = f"({s1}{i}{s2})"
            stack.append(bT)
    print("".join(stack))
