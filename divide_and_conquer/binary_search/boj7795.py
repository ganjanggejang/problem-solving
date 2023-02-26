from sys import stdin
from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    b.sort()

    cnt = 0
    for x in a:
        cnt += bisect_left(b, x)

    print(cnt)
