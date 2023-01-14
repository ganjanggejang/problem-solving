import heapq
import sys

pq = []
n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(pq, (-x, x))  # 최대 힙이라 우선순위를 부여
    else:
        if len(pq) == 0:
            print(0)
        else:
            print(heapq.heappop(pq)[1])
