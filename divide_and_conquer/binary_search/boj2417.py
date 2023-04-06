"""
결정 문제: "mid**2이 n보다 큰가?"로 잡아주면 
결정 문제의 분포는 ffffttttt가 된다

"""

n = int(input())

lo = 0
hi = n

while lo + 1 < hi:
  mid = (lo+hi)//2

  # ffffffffttt
  if mid**2 >= n: hi = mid
  else: lo = mid

print(hi)
