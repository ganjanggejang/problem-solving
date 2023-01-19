from collections import deque

a, b = map(int, input().split())

ans = -1
q = deque()
q.append((a, 0))
while q:
    now, cnt = q.popleft()
    if now == b:
        ans = cnt
        break
    if now * 2 <= b:
        q.append((now * 2, cnt + 1))
    if now * 10 + 1 <= b:
        q.append((now * 10 + 1, cnt + 1))

if ans == -1: print(-1)
else: print(ans + 1)
