from collections import deque

a, b, c = map(int, input().split())


def bfs(a, b, ans):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x == ans and y == ans:
            return True

        if check[x][y]: continue

        check[x][y] = True
        now = [x, y, total - (x + y)]
        for i in range(3):
            for j in range(3):
                if now[i] < now[j]:
                    next = [x, y, total - (x + y)]
                    next[i] += now[i]
                    next[j] -= now[i]
                    q.append((next[0], next[1]))
    return False


total = a + b + c
ans = total // 3
if total % 3 != 0:
    print(0)
else:
    check = [[False] * 1501 for _ in range(1501)]

    if bfs(a, b, ans):
        print(1)
    else:
        print(0)
