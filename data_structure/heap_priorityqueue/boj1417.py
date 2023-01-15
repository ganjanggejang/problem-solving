import heapq
import sys

candidate = []  # 기호1을 제외한 나머지 후보가 들어가는 우선순위큐
n = int(input())
number1 = int(input())  # 기호1
for _ in range(n - 1):
    x = int(sys.stdin.readline())
    heapq.heappush(candidate, -x)  # 내림차순

count = number1

# 기호1을 따로 변수에 빼놓으면 리스트의 0번째(기호1)를 제외한 나머지 사이에 최댓값이 또 있는지 확인할 필요가 x
if len(candidate) != 0:
    while True:
        temp = -heapq.heappop(candidate)  # 최대힙이기 때문에 pop되는건 항상 최댓값
        if number1 > temp:
            break
        number1 += 1
        temp -= 1
        heapq.heappush(candidate, -temp)

# for문으로 돌리면 1 ~ len(candidate) 돌리는 사이에 이미 요건이 충족되어도 끝까지 돌아가야하기 때문에 답을 놓치게 됨
count = number1 - count
print(count)
