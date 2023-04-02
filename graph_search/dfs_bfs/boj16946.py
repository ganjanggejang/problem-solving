from collections import deque
import sys

n, m = map(int, input().split())
graph = []  # 0은 탐색하지않은빈방, 1은 벽, 2 이상부터 탐색된 빈방의 그룹 번호

for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(st_x, st_y, group_num):
    q = deque()
    q.append((st_x, st_y))
    graph[st_x][st_y] = group_num
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    cnt += 1
                    graph[nx][ny] = group_num
                    q.append((nx, ny))

    return cnt % 10


group_room_cnt = [-1, -1]  # 그룹 번호 2번부터 시작, 각 그룹에 속한 빈방의 개수 들어감
group_num = 2
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:  # 빈 칸 그룹화
            group_room_cnt.append(bfs(i, j, group_num))
            group_num += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 벽의 상하좌우 검사
            near = set()
            ans = 1
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if graph[ni][nj] >= 2:  # 벽의 인접칸에 빈방이 있다면:
                        near.add(graph[ni][nj])

            for num in near:
                ans += group_room_cnt[num]
            print(ans % 10, end='')
        else:
            print(0, end='')
    print()
