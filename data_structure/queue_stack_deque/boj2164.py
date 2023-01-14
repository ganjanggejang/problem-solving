from collections import deque

n = int(input())
deq = deque([x for x in range(1, n + 1)])

while len(deq) > 1:
    deq.popleft()
    temp = deq.popleft()
    deq.append(temp)

print(deq[0])
