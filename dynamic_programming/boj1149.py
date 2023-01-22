"""
테이블 정의하기
d[i][0] = i번째까지의 최소 비용, i번째 집은 red
d[i][1] = i번째까지의 최소 비용, i번째 집은 green
d[i][2] = i번째까지의 최소 비용, i번째 집은 blue

점화식 찾기
d[k][0] = min(d[k-1][1], d[k-1][2]) + red[k]
d[k][1] = min(d[k-1][0], d[k-1][2]) + green[k]
d[k][2] = min(d[k-1][0], d[k-1][1]) + blue[k]

초기값 설정하기
d[1][0] = red[1]
d[1][1] = green[1]
d[1][2] = blue[1]
"""
import sys

n = int(input())
red = [0]
green = [0]
blue = [0]

for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    red.append(r)
    green.append(g)
    blue.append(b)

d = [[0] * 3 for _ in range(1001)]
d[1][0] = red[1]
d[1][1] = green[1]
d[1][2] = blue[1]

for k in range(2, n + 1):
    d[k][0] = min(d[k - 1][1], d[k - 1][2]) + red[k]
    d[k][1] = min(d[k - 1][0], d[k - 1][2]) + green[k]
    d[k][2] = min(d[k - 1][0], d[k - 1][1]) + blue[k]

print(min(d[n][0], d[n][1], d[n][2]))
