import sys

n = int(input())
m = int(input())
graph = {}
visited = []
check_visited = [False] * (n + 1)


def dfs(v):
    visited.append(v)
    check_visited[v] = True
    for child in graph[v]:
        if check_visited[child] == False:
            dfs(child)
    return


for i in range(1, n + 1):
    graph[i] = []
for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs(1)
print(len(visited) - 1)
