# check[index]랑 cycle_start랑 헷갈리면 안됨
from collections import deque
import sys

sys.setrecursionlimit(10**6)
n = int(input())
graph = {}
check = [0] * n  # 0: not visited, 1: visited, 2: cycle

# graph 정보 입력, 0-based
for i in range(n):
    graph[i] = []
for _ in range(n):
    node1, node2 = map(int, sys.stdin.readline().split())
    node1 -= 1
    node2 -= 1
    graph[node1].append(node2)
    graph[node2].append(node1)

### 1단계: 순환선 찾기
# dfs
"""
-2: 사이클 찾은 상태, 해당 정점은 사이클에 포함되지 않음
-1: 사이클 못 찾은 상태
0 ~ n-1: 사이클 찾은 상태, 사이클의 시작 인덱스
"""


def dfs(now, previous):
    if check[now] == 1:  # 이미 방문한 정점을 다시 방문하면 그 정점 번호를 return
        return now

    check[now] = 1  # 방문 표시
    for next in graph[now]:
        if next == previous:  # 바로 이전 정점은 탐색x
            continue
        cycle_start = dfs(next, now)
        if cycle_start == -2:  # 사이클 찾은 상태, 해당 정점은 사이클에 포함되지 않음
            return -2
        if cycle_start >= 0:  # 사이클 찾은 상태, 해당 정점은 사이클에 포함됨
            check[now] = 2  # 사이클에 포함된다는 표시
            if now == cycle_start:  # 현재 정점이 사이클 시작 정점과 같으면, 지금부터 리턴되는 정점들은 사이클에 포함시켜주면 안되므로 -2 리턴
                return -2
            else:  # 아직 사이클을 찾지 못했으므로 그냥 cycle_start 리턴
                return cycle_start
    return -1


dfs(0, -1)

### 2단계: 순환선으로부터 떨어진 거리 찾기
q = deque()
distance = [-1] * n

for i in range(n):
    if check[i] == 2:  # 사이클에 포함되는 정점이라면:
        distance[i] = 0
        q.append(i)
    else:
        distance[i] = -1

# bfs
while q:
    x = q.popleft()
    for child in graph[x]:
        if distance[child] == -1:
            q.append(child)
            distance[child] = distance[x] + 1

# 문제 요구사항대로 수행
for value in distance:
    print(value, end=' ')
