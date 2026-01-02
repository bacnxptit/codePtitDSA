n = int(input())
for i in range(n):
    k = int(input())
    s = input().strip().split()
    stack = []
    for i in s[::-1]:
        if i.lstrip('-').isdigit() :
            stack.append(int(i))
        else:
            s2 = stack.pop()
            s1 = stack.pop()
            if i == '+':
                stack.append(s2+s1)
            elif i == '-':
                stack.append(s2-s1)
            elif i == '*':
                stack.append(s2*s1)
            elif i == '/':
                stack.append(int(s2/s1))
    print(stack[0])