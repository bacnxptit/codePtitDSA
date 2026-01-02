n = int(input())
for _ in range(n):
    n = int(input())
    s = input().strip().split()
    stack = []
    if s[-1].lstrip('-').isdigit() :
        for i in s[::-1]:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if i == '+':
                    stack.append(s2+s1)
                elif i == '-':
                    stack.append(-s2+s1)
                elif i == '*':
                    stack.append(s2*s1)
                elif i == '/':
                    stack.append(int(s2/s1))
    else:
        for i in s:
            if i.isdigit():
                stack.append(int(i))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if i == '+':
                    stack.append(s2+s1)
                elif i == '-':
                    stack.append(s2-s1)
                elif i == '*':
                    stack.append(s2*s1)
                elif i == '/':
                    stack.append(int(s2/s1))
    print(stack[0])
