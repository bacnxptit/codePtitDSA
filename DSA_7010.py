n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    for i in s[::-1] :
        if i.isalnum():
            stack.append(i)
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            new = s1+s2+i
            stack.append(new)
    print("".join(stack))