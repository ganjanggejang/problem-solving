import sys


def check(i):
    cnt = 0
    for x in lan:
        cnt += x // i

    return cnt >= n  # true or false


k, n = map(int, input().split())

lan = []
max_lan = 0
for _ in range(k):
    x = int(sys.stdin.readline())
    max_lan = max(max_lan, x)
    lan.append(x)

# 이분 탐색 진행
lo = 1
hi = max_lan + 1
while lo + 1 < hi:  # lo랑 hi 사이는 2칸 이상 있어야함, lo랑 hi는 ttt..tffff tf 바뀌는 그 두 지점을 가리킴.
    mid = (lo + hi) // 2

    if check(mid): lo = mid
    else: hi = mid

print(lo)  # n개를 만들 수 있는 랜선의 최대 길이 -> t인 최대 지점 -> lo
