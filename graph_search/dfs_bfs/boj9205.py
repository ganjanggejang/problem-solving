import sys
from collections import deque

t = int(input())


def check(st_x, st_y, en_x, en_y):
    if abs(en_x - st_x) + abs(en_y - st_y) <= 1000:
        return True
    else:
        return False


for _ in range(t):
    n = int(sys.stdin.readline())
    now_x, now_y = map(int, sys.stdin.readline().split())
    market = []  # [x, y, visited], visited = 0(미방문) or 1(방문)
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        market.append([x, y, 0])
    festival_x, festival_y = map(int, sys.stdin.readline().split())

    ans = False
    if check(now_x, now_y, festival_x, festival_y):
        ans = True
    else:
        q = deque()
        q.append((now_x, now_y))
        while q:
            x, y = q.popleft()
            if check(x, y, festival_x, festival_y):
                ans = True
                break

            for i in range(len(market)):
                if check(market[i][0], market[i][1], x,
                         y) and market[i][2] == 0:
                    q.append((market[i][0], market[i][1]))
                    market[i][2] = 1  # 방문표시

    if ans: print("happy")
    else: print("sad")
