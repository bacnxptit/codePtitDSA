n =int(input())
for i in range(n):
    str = input().strip().split()
    stack  =[]
    res = []
    for s in str :
        stack.append(s)
    while stack :
        res.append(stack.pop())
    print(" ".join(res))


