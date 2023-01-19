from collections import deque
import sys
n = int(input())
graph = []


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    cnt = 1
    graph[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt


for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(row)

apart = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            apart.append(bfs(i, j))

apart.sort()
print(len(apart))
for num in apart:
    print(num)
