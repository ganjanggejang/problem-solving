import heapq
import sys

n = int(input())
graph = []
pq = []

for _ in range(n):
    row = map(int, sys.stdin.readline().split())
    if len(pq) == 0:
        for num in row:
            heapq.heappush(pq, num)
    else:
        for num in row:
            if pq[0] < num:
                heapq.heappush(pq, num)
                heapq.heappop(pq)

print(pq[0])
