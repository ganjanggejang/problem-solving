import sys

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = []
check = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

# dfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt, color):
    if check[x][y]:
        return cnt - distance[x][y] >= 4  # True or False 가 return됨 # 여기가 핵심

    check[x][y] = True
    distance[x][y] = cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == color:
                if dfs(nx, ny, cnt + 1, color):  # if True:
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
            if dfs(i, j, 0, graph[i][j]):
                print("Yes")
                is_break = True
                break
    if is_break:
        break

if not is_break:
    print("No")
