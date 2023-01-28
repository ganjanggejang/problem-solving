import sys

sys.setrecursionlimit(10**6)
k = int(input())


# dfs
def dfs(v, group_num):
    check[v] = group_num
    for child in graph[v]:
        if check[child] == 0:
            dfs(child, -group_num)
        if check[child] == group_num:
            global bipartite
            bipartite = False
    return


for _ in range(k):
    graph = {}
    v, e = map(int, sys.stdin.readline().split())

    # graph 정보 입력
    for i in range(1, v + 1):
        graph[i] = []
    for _ in range(e):
        node1, node2 = map(int, sys.stdin.readline().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    # 문제 요구사항대로 수행
    check = [0] * (v + 1)
    bipartite = True
    for i in range(1, v + 1):
        if check[i] == 0:
            dfs(i, 1)
        if not bipartite: break

    if bipartite: print("YES")
    else: print("NO")
