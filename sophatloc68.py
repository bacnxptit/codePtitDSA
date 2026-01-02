n = int(input())
for _ in range(n):
    n = int(input())
    res = []
    def backTrack(path):
        if 1 <= len(path )<= n:
            res.append("".join(map(str,path)))
        if len(path)==n:
            return
        path.append('6')
        backTrack(path)
        path.pop()

        path.append('8')
        backTrack(path)
        path.pop()

    backTrack([])

    res.sort(key=lambda x:int(x))

    print(len(res))
    for i in res :
        print(i,end=" ")
    print()


    