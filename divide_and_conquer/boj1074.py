import sys

sys.setrecursionlimit(10**6)

n, x, y = map(int, input().split())


def go(n, x, y):
    if n == 1:
        return 2 * x + y  # 0, 1, 2, 3
    else:
        if x < 2**(n-1):
            if y < 2**(n-1):  # 2사분면
                return go(n-1, x, y) + 2**(2*n - 2) * 0
            else:  # 1사분면
                return go(n-1, x, y - 2**(n-1)) + 2**(2*n - 2)*1

        else:
            if y < 2**(n - 1):  # 3사분면
                return go(n-1, x - 2**(n-1), y) + 2**(2*n - 2)*2
            else:  # 4사분면
                return go(n-1, x - 2**(n-1),
                          y - 2**(n-1)) + 2**(2*n - 2)*3


print(go(n, x, y))
