n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    for i in s[::-1] :
        if i.isdigit():
            stack.append(int(i))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            if i == "+":
                stack.append(s1+s2)
            elif i == "-":
                stack.append(s1-s2)
            elif i == "*":
                stack.append(s1*s2)
            elif i == "/":
                stack.append(s1//s2)
    print(*stack)