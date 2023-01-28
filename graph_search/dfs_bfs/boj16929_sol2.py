import sys

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = []
check = [[False] * m for _ in range(n)]

# dfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, px, py, color):  # previous_x, previous_y
    if check[x][y]:
        return True  # 바로 이전 칸을 제외한 다른 칸으로 이동하다가, 이미 방문한 칸을 다시 방문하면 반드시 사이클이 존재하는거임

    check[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not (nx == px and ny == py) and graph[nx][ny] == color:
                if dfs(nx, ny, x, y, color):
                    return True

    return False


# graph 정보 입력
for _ in range(n):
    user_input = list(map(str, input()))
    graph.append(user_input)

# 문제 요구사항대로 수행
is_break = False
for i in range(n):
    for j in range(m):
        if not check[i][j]:
            if dfs(i, j, -1, -1, graph[i][j]):
                print("Yes")
                is_break = True
                break
    if is_break:
        break

if not is_break:
    print("No")
