def sinhhoavi(s):
    n = len(s)
    use = [False] * n
    crr= []
    def backtrack():
        if len(crr) == n :
            print("".join(map(str,crr)),end = " ")
            return
        for i in range(n):
            if not use[i] :
                use[i] = True
                crr.append(s[i])
                backtrack()
                crr.pop()
                use[i] = False
    backtrack()

n = int(input())
for _ in range(n):
    s = input()
    sinhhoavi(s)
    print()
"""
def sinhxauhoanvi(s):
    n =len(s)
    use = [False]*n
    arr = []
    def backtrack():
        if len(arr) == n :
            print("".join(map(str,arr)),end = " ")
            return
        for i in range(n):
            if not use[i] :
                use[i]  = True
                arr.append(s[i])
                backtrack()
                arr.pop()
                use[i] = False
    backTrack()
t = int(input))
for _ in range(t):
    s = input() 
    sinhxauhoanvi(s)
    print()
    
    
    
    
def sinhxauhoanvi(s):
    n = len(s)
    use = [False] * n
    arr = {}
    def backTrack():        
        if len(arr) == n:
            print("".join(map(str,arr)), end = " ")
            return
        for i in range(n):
            if not use[i] :
                use[i] = True
                arr.append(s[i])
                backtrack()
                arr.pop()
                use[i] = False
    backTrack()  
    
t = int(input())
for _ in range(t):
    s = input()
    sinhxauhoanvi(s)
    print()          
"""
