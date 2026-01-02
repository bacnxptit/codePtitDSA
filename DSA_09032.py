def solve():
    n ,m = int(input())
    gird = [list(input().strip() for _ in range(n))]
    visited = [ [False]*n for _ in range(n) ]
    direction = [
        (-1,-1),(-1,0),(-1,1),
        (0,-1),(0,0),(0,1),
        (1,-1),(1,0),(1,1)
    ]
    