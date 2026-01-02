n= int(input())
for _ in range(n):
    s  = input().strip()
    stack = [1]
    sign = 1
    res = []
    for i in s:
        if i == "+":
            sign =stack[-1]
        elif i == "-":
            sign = - stack[-1]
        elif i == "(" :
            stack.append(sign)
        elif i == ")" :
            stack.pop()
        else:
            if sign  == 1 :
                res.append('+'+i)
            else:
                res.append('-'+i)

    result = "".join(res)
    if result[0] == "+":
        result = result[1:]
    print(result)
"""
s =input()
stack = [1]
res =[]
sign = 1
for i in s:
    if i == "+":
        sign = stack[-1]:
    elif  i == "-":
        sign = -stack[-1]
    elif i == "(":
        stack.append(sign)
    elif i == ")":
        stack.pop()
    else:
        if sign  == 1 :
            res.append('+'+i)
        else:
            res.append('-'+i)
    result = "".join(res)
    if result[0] == "+":
        result = result[1:]
    print result
    
        
"""