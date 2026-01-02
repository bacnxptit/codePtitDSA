def count_islands(N, M, A):
    visited = [[False] * M for _ in range(N)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    count = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1 and not visited[i][j]:
                # DFS dùng stack
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and A[nx][ny] == 1:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                count += 1
    return count

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(count_islands(N, M, A))
