from collections import deque
import sys

n = int(input())
m = int(input())
graph = {}
visited = []
check_visited = [False] * (n + 1)


def bfs(start_v):
    queue = deque([start_v])
    visited.append(start_v)
    check_visited[start_v] = True
    while queue:
        v = queue.popleft()
        for child in graph[v]:
            if check_visited[child] == False:
                queue.append(child)
                visited.append(child)
                check_visited[child] = True
    return


for i in range(1, n + 1):
    graph[i] = []
for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

bfs(1)
print(len(visited) - 1)
