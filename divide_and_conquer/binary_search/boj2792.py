import sys


def check(mid):
    cnt = 0
    for x in marble:
        while x > 0:
            x -= mid
            cnt += 1

    return cnt <= n


n, m = map(int, input().split())
marble = []
for _ in range(m):
    x = int(sys.stdin.readline())
    marble.append(x)


lo = 0
hi = max(marble) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2

    if check(mid): hi = mid
    else: lo = mid

print(hi)
