from collections import deque

s = int(input())
dist = [[-1] * (2001) for _ in range(2001)]  # why 2000?

q = deque()
q.append((1, 0))
dist[1][0] = 0
while q:
    now, clipboard = q.popleft()
    if now == s:
        break

    if now > 0:  # 3. 이모티콘 삭제
        next = now - 1
        if dist[next][clipboard] == -1:
            dist[next][clipboard] = dist[now][clipboard] + 1
            q.append((next, clipboard))

    if now + clipboard <= 1001:  # 2. 이모티콘 붙여넣기
        next = now + clipboard
        if dist[next][clipboard] == -1:
            dist[next][clipboard] = dist[now][clipboard] + 1
            q.append((next, clipboard))

    if now > 0:  # 1. 이모티콘 복사
        next = now
        next_clip = now
        if dist[next][next_clip] == -1:
            dist[next][next_clip] = dist[now][clipboard] + 1
            q.append((next, next_clip))

ans = 1001
for num in dist[s]:
    if num != -1:
        ans = min(ans, num)
print(ans)
