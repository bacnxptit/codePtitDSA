s = input().strip()
stack =[]
total = 0
for i in s :
    if i == "(":
        stack.append(i)
        print(stack)
    else:
        if  stack :
            stack.pop()
            total += 2
print(total)