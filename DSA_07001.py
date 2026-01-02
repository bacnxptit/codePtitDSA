import sys;
stack = []
for line  in sys.stdin :
    line = line.strip()
    if not line:
        continue
    part = line.split()
    if part[0] == 'push':
        x = int(part[1])
        if x < 1000 :
            stack.append(x)
    elif part[0] == 'pop':
        if stack:
            stack.pop()
    elif part[0] == 'show':
        if not stack :
            print('empty')
        else:
            print(" ".join(map(str,stack)))