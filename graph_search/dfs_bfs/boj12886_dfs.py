import sys

sys.setrecursionlimit(1501 * 1501)
a, b, c = map(int, input().split())


def dfs(a, b):
    if check[a][b]:
        return
    check[a][b] = True
    now = [a, b, total - (a + b)]
    for i in range(3):
        for j in range(3):
            if now[i] < now[j]:
                next = [a, b, total - (a + b)]
                next[i] += now[i]
                next[j] -= now[i]
                dfs(next[0], next[1])


total = a + b + c
if total % 3 != 0:
    print(0)
else:
    check = [[False] * 1501 for _ in range(1501)]
    dfs(a, b)
    if check[total // 3][total // 3]:
        print(1)
    else:
        print(0)
