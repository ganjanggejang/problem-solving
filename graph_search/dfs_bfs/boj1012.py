from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
    return


t = int(input())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())  # 가로 m, y 세로 n, x
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
