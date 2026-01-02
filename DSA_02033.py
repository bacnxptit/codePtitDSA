def soxacach(n):
    use = [False] * (n+1)
    arr = []

    def backtrack():
        if len(arr) == n :
            print("".join(map(str,arr)))
            return
        for i in range(1,n+1) :
            if not use[i] :
                if arr and abs(arr[-1]-i) == 1 :
                    continue
                use[i] = True
                arr.append(i)
                backtrack()
                arr.pop()
                use[i] = False
    backtrack()
t  = int(input())
for _ in range(t) :
    n = int(input())
    soxacach(n)
    print()