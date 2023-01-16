import sys
import heapq

lecture = []
n = int(input())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())  # s, t
    heapq.heappush(lecture, (start, end - 1))

classroom = [-1]  # 각 요소는 각 교실의 수업 마치는 시간
# 시간의 흐름
now = 0
while len(lecture) != 0:
    runtime = heapq.heappop(lecture)  # (start, end)
    if runtime[0] <= now <= runtime[1]:
        if runtime[0] > classroom[0]:  # 기존 교실그대로사용가능
            heapq.heappop(classroom)
            heapq.heappush(classroom, runtime[1])
        else:  # 새로운 교실만들어야함
            heapq.heappush(classroom, runtime[1])

    else:
        now = runtime[0]
        heapq.heappush(lecture, runtime)  # 처리안된수업은 다시 넣어줌

print(len(classroom))
