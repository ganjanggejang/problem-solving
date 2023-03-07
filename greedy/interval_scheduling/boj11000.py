"""
시간의 흐름에 따라 다음을 고려한다. 
매 시각 t에 시작하는 작업이 있을 때 지금까지 구매한 기계에 할당할 수 있으면 
그것들 중 아무 것에 할당한다. 
현재까지 구매한 기계만으로는 불가능하다면, 
기계를 하나 더 구매하고 거기에 할당한 다음 t⋆←t를 기억한다.
"""

import sys
import heapq

lecture = []
n = int(input())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(lecture, (start, end - 1))

classroom = [-1]  # 각 요소는 각 교실의 수업 마치는 시간
# 시간의 흐름
now = 0
while len(lecture) != 0:
    st, en = heapq.heappop(lecture)
    if st <= now <= en:
        if st > classroom[0]:  # 기존 교실그대로사용가능
            heapq.heappop(classroom)
            heapq.heappush(classroom, en)
        else:  # 새로운 교실만들어야함
            heapq.heappush(classroom, en)

    else:
        now = st
        heapq.heappush(lecture, (st, en))  # 처리안된수업은 다시 넣어줌

print(len(classroom))
