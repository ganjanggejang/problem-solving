from sys import setrecursionlimit
setrecursionlimit(10**6)


def power(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power(x, n // 2, mod)
        return (y * y) % mod
    else:
        y = power(x, (n - 1) // 2, mod)
        return (x * y * y) % mod


a, b, c = map(int, input().split())

print(power(a, b, c))
