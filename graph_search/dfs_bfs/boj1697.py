from collections import deque

n, k = map(int, input().split())
check = [False] * 100001
dist = [-1] * 100001

q = deque()
q.append(n)
check[n] = True
dist[n] = 0
while q:
    now = q.popleft()
    if now - 1 >= 0:
        if check[now - 1] == False:
            q.append(now - 1)
            check[now - 1] = True
            dist[now - 1] = dist[now] + 1
    if now + 1 < 100001:
        if check[now + 1] == False:
            q.append(now + 1)
            check[now + 1] = True
            dist[now + 1] = dist[now] + 1
    if now * 2 < 100001:
        if check[now * 2] == False:
            q.append(now * 2)
            check[now * 2] = True
            dist[now * 2] = dist[now] + 1

print(dist[k])
