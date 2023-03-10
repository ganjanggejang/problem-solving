"""
매번 공용 기계로부터 신호를 받으면(닭이 건널 시각이 되면), 
처리할 수 있는 작업(소가 건널 수 있는 시간) 중 
가장 마감 시각이 이른 것을 공용 기계로 전송한다.
만약 처리할 수 있는 작업이 존재하지 않는 경우에는 아무 행동도 하지 않는다.
"""

import sys
import heapq

c, n = map(int, input().split())

chicken_time = []
for _ in range(c):
    t = int(sys.stdin.readline())
    chicken_time.append(t)

chicken_time.sort()

cow_runtime = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())  # a, b
    heapq.heappush(cow_runtime, (start, end))

now = 0
count = 0

for now in chicken_time:
    if len(cow_runtime) == 0:
        break

# now에 건너갈 수 있는 소들을 모두 runtime_in_now에 저장
    runtime_in_now = []
    for start, end in cow_runtime:
        if start <= now <= end:
            heapq.heappush(runtime_in_now, (end, start))  # end 기준으로 최소힙

# now에 건너갈 수 있는 소가 1마리 이상이라도 있을 때,
# 그 중 end가 최소인 소 한마리만 택해서 remove
    if len(runtime_in_now) != 0:
        end, start = heapq.heappop(runtime_in_now)
        cow_runtime.remove((start, end))
        count += 1

print(count)
