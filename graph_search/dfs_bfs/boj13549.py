from collections import deque

n, k = map(int, input().split())
check = [False] * 100001
dist = [-1] * 100001  # 방문여부 + 거리 동시에 표시하는 리스트

q = deque()
q.append(n)
check[n] = True
dist[n] = 0
while q:
    now = q.popleft()
    if now * 2 < 100001:
        if check[now * 2] == False:
            q.appendleft(now * 2)  # 간선가중치가 0이므로 큐의 앞에 넣음 (다음반복때 바로 pop되도록)
            check[now * 2] = True
            dist[now * 2] = dist[now]  # 가중치0이므로 시간+1 안해줌
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

print(dist[k])
