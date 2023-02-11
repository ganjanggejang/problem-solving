from collections import deque
import sys

n, m = map(int, input().split())
# dist[x][y][0]은 벽 파괴 가능, dist[x][y][1]은 불가능
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
graph = []

# graph 정보 입력
for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(row)

# bfs
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

ans = -1
while q:
    x, y, broken = q.popleft()
    # 끝 점에 도달하면 이동 횟수를 출력
    if (x, y) == (n - 1, m - 1):
        ans = dist[x][y][broken]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
        if graph[nx][ny] == 1 and not broken:
            dist[nx][ny][1] = dist[x][y][0] + 1
            q.append((nx, ny, 1))
        # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
        if graph[nx][ny] == 0 and dist[nx][ny][broken] == -1:
            dist[nx][ny][broken] = dist[x][y][broken] + 1
            q.append((nx, ny, broken))

print(ans)
