"""
정점 -> 정점으로 이동할 때, 항상 이동할 수 있어야함
A에서 B로 어떨 땐 갈 수 있고 어떨 땐 갈 수 없다면 
그건 다른 정점이라고 해줘야함!

정점 분리 해줘야함
(x, y) 말고 (x, y, z)로. (z는 벽 1회 제거 여부)
(0, 0, 0)과 (0, 0, 1)은 다른 정점

(이모티콘 문제와 유사)

"""

from collections import deque
import sys

n, m = map(int, input().split())
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
graph = []

for _ in range(n):
    user_input = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(user_input)

# bfs
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

ans = -1
while q:
    x, y, broken = q.popleft()

    if (x, y) == (n - 1, m - 1):
        ans = dist[x][y][broken]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 1 and not broken:
            dist[nx][ny][1] = dist[x][y][0] + 1
            q.append((nx, ny, 1))

        if graph[nx][ny] == 0 and dist[nx][ny][broken] == -1:
            dist[nx][ny][broken] = dist[x][y][broken] + 1
            q.append((nx, ny, broken))

print(ans)
