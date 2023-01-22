"""
테이블 정의하기
d[i][j] = 현재 j개의 계단을 연속해서 밟고서, i번째 계단을 밟았을 때의 최대 점수

점화식 찾기
d[k][1] = max(d[k-2][1], d[k-2][2]) + stair[k]
d[k][2] = d[k-1][1] + stair[k]
...
마지막 계단 n
answer = max(d[n][1], d[n][2])

초기값 설정하기
d[1][1] = stair[1], d[1][2] = 0, 
d[2][1] = stair[2], d[2][2] = stair[1] + stair[2]
"""
import sys

n = int(input())
stair = [0] * 301

for i in range(1, n + 1):
    point = int(sys.stdin.readline())
    stair[i] = point

# d[i][j] i : 0~301 j : 0~2
d = [[0] * 3 for _ in range(301)]
d[1][1] = stair[1]
d[1][2] = 0
d[2][1] = stair[2]
d[2][2] = stair[1] + stair[2]

if n == 1:
    print(d[1][1])
elif n == 2:
    print(max(d[2][1], d[2][2]))
else:
    for i in range(3, n + 1):
        d[i][1] = max(d[i - 2][1], d[i - 2][2]) + stair[i]
        d[i][2] = d[i - 1][1] + stair[i]

    print(max(d[n][1], d[n][2]))
