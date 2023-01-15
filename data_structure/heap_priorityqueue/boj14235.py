import heapq
import sys

n = int(input())
pq = []  # 최대 힙

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if len(a) == 1 and a[0] == 0:
        if len(pq) == 0:
            print(-1)
        else:
            print(-pq[0])
            heapq.heappop(pq)
    else:
        for i in range(1, len(a)):
            heapq.heappush(pq, (-(a[i])))
