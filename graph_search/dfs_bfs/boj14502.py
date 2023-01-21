from collections import deque
import sys

n, m = map(int, input().split())
graph = []
virus = []
room = 0

# graph 정보 입력
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if row[j] == 0:
            room += 1
        if row[j] == 2:
            virus.append((i, j))
    graph.append(row)

# bfs (바이러스 최대영역 구하기)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    cnt = 0
    check = [[0] * m for _ in range(n)]
    q = deque()
    for v in virus:
        q.append(v)
        check[v[0]][v[1]] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not check[nx][ny]:
                    cnt += 1
                    check[nx][ny] = 1
                    q.append((nx, ny))

    return cnt


# 벽 세우기
max_safe_area = 0
for w_one in range(n * m - 2):
    if graph[w_one // m][w_one % m] == 0:
        graph[w_one // m][w_one % m] = 1

        for w_two in range(w_one + 1, n * m - 1):
            if graph[w_two // m][w_two % m] == 0:
                graph[w_two // m][w_two % m] = 1

                for w_three in range(w_two + 1, n * m):
                    if graph[w_three // m][w_three % m] == 0:
                        graph[w_three // m][w_three % m] = 1
                        max_safe_area = max(max_safe_area, room - bfs() - 3)
                        graph[w_three // m][w_three % m] = 0

                graph[w_two // m][w_two % m] = 0

        graph[w_one // m][w_one % m] = 0

print(max_safe_area)
