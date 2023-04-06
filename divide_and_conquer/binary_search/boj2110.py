"""
공유기 사이의 거리들의 최솟값이 최대인 경우를 구하라

결정 문제: 인접한 공유기 사이가 mid 이상이 되도록 공유기를 c개 이상 배치할 수 있는가?
결정문제분포: tttttttttfffff

check 함수: 공유기를 c개 이상 배치할 수 있는가 -> 
공유기를 가능한 최대로 많이 배치하여 그게 m개 이상인지만
확인해주면 됨
-> 무조건 첫번째 집에 공유기 설치한 뒤, 거리가 mid 이상이 될 때마다 하나씩 더 설치해주면 됨 (greedy)
"""
import sys


def check(mid):
  	cnt = 1  # 첫번째 집에 공유기 설치
  	i = 0
  	j = 1
  	while j < n:
  		if house[j] - house[i] >= mid:
  			i = j
  			cnt += 1
  
  		j += 1
  
  	return cnt >= c


n, c = map(int, input().split())
house = []
for _ in range(n):
  	house.append(int(sys.stdin.readline()))

house.sort()

lo = 1
hi = house[-1] + 1

while lo + 1 < hi:
  	mid = (lo + hi) // 2
  	if check(mid): lo = mid
  	else: hi = mid

print(lo)
