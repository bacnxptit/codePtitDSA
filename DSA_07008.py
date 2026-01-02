n =int(input())
for _ in range(n):
    s = input().strip()
    res = []
    stack = []
    level = {
        "+":"1",
        "-": "1",
        "*": "2",
        "/": "2",
        "^": "3"
    }
    for i in s:
        if i.isalnum():
            res.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")" :
            while stack and stack[-1] != "(":
                res.append(stack.pop())
            stack.pop()
        else:
            while( stack and stack[-1] != "(" and level[stack[-1]] >= level[i]):
                res.append(stack.pop())
            stack.append(i)
    while stack :
        res.append(stack.pop())
    print("".join(res))