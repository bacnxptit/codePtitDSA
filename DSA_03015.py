import math
def muaLuongthuc(n,s,m):
    if n < m :
        return -1
    closed = s // 7
    open_day = s-closed
    need = s * m
    if open_day*n < need :
        return -1
    else:
        return math.ceil(need/n)
n = int(input())
for i in range(n):
    n,s,m = map(int,input().split())
    print(muaLuongthuc(n,s,m))
