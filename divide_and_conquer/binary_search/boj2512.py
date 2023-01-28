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
