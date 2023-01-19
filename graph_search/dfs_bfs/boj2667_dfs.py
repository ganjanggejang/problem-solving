import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = []


def dfs(x, y):
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1:
            global cnt
            cnt += 1
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

    return


for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(row)

apart = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            apart.append(cnt)
            cnt = 0

apart.sort()
print(len(apart))
for i in apart:
    print(i)
