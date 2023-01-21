# bfs - 시작점이 여러 개일 때: 모든 시작점을 하나의 bfs 속 큐에 넣고 돌리면 됨
from collections import deque
import sys

m, n = map(int, input().split())
graph = []
ripe_tomato_location = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
cnt = 0


def bfs():
    global cnt

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    cnt = graph[nx][ny]
                    q.append((nx, ny))


for x_coor in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for y_coor in range(len(row)):
        # 큐에 익토 위치 넣기
        if row[y_coor] == 1:
            q.append((x_coor, y_coor))
    graph.append(row)

bfs()

fully_riped = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            fully_riped = False

if fully_riped:
    if cnt == 0: print(cnt)
    else: print(cnt - 1)
else:
    print(-1)
