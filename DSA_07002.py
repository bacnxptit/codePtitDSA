
n = int(input())
stack = []
for i in range(n):
    line = input().strip()
    if line.split()[0] == "PUSH" :
        if int(line.split()[1]) < 1000 :
            stack.append(int(line.split()[1]))
    elif line.split()[0] == "PRINT" :
       if not stack :
           print('NONE')
       else:
           print(stack[-1])
    elif line.split()[0] == 'POP':
            if stack:
                stack.pop()
