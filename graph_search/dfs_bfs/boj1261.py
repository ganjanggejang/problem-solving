from collections import deque
import sys

m, n = map(int, input().split())
dist = [[-1] * m for _ in range(n)]  # 방문여부 + 거리 동시에 표시하는 리스트
graph = []

# graph 정보 입력
for _ in range(n):
    user_input = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(user_input)

# bfs
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:  # 방문하지 않은 점에 대해:
                if graph[nx][ny] == 0:  # 빈방일때 -> 가중치 0 -> appendleft
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:  # 벽일때 -> 가중치 1 -> append
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

print(dist[n - 1][m - 1])
