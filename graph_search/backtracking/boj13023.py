import sys

sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = {}

# dfs(backtracking)
abcde = False


def dfs(v, depth):
    if depth == 5:
        global abcde
        abcde = True
        return
    for child in graph[v]:
        if not check[child]:
            check[child] = True
            dfs(child, depth + 1)
            check[child] = False
    return


# graph 정보 입력
for i in range(0, n):
    graph[i] = []
for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 문제 요구사항대로 수행
for i in range(n):
    check = [False] * n
    check[i] = True
    dfs(i, 1)
    if abcde:
        print(1)
        break

if not abcde:
    print(0)
