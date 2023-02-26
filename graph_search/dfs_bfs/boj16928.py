import sys
from collections import deque

n, m = map(int, input().split())

dist = [-1] * 101  # 1-based # -1은 미방문, 1이상은 최소횟수
jump = {}  # 해당숫자로 순간이동(key -> value)

for _ in range(n + m):
    x, y = map(int, sys.stdin.readline().split())
    jump[x] = y

q = deque()
q.append(1)
dist[1] = 0

is_break = False
while q:
    now = q.popleft()
    for i in range(1, 7):
        if dist[100] != -1:
            is_break = True
            break

        if now + i <= 100:
            if dist[now + i] == -1:
                if now + i in jump.keys() and dist[jump[now + i]] == -1:
                    q.append(jump[now + i])
                    dist[jump[now + i]] = dist[now] + 1
                if now + i not in jump.keys() and dist[now + i] == -1:
                    q.append(now + i)
                    dist[now + i] = dist[now] + 1

    if is_break: break

print(dist[100])
