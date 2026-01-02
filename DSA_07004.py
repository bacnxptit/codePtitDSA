import math
n = int(input())

for _ in range(n):
    s  =input().strip()
    stack = []

    for i in s :
        if i == "(":
            stack.append(i)
        else:
           if stack and  stack[-1] == "(" :
               stack.pop()
           else:
               stack.append(i)
    dem1 = stack.count('(')
    dem2 =stack.count(')')
    l = math.ceil(dem1/2) +math.ceil(dem2/2)
    print(l)


