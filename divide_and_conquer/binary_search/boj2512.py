"""
결정 문제: "상한을 mid로 했을 때 예산 분배가 가능한가?"로 잡아주면 
결정 문제의 분포는 tttttffffff
"""

def check(mid):
    cnt = 0
    for x in budget:
        if x >= mid:
            cnt += mid
        else:
            cnt += x

    return cnt <= m


n = int(input())
budget = list(map(int, input().split()))
m = int(input())

lo = 0
hi = max(budget) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2

    if check(mid): lo = mid
    else: hi = mid

print(lo)
