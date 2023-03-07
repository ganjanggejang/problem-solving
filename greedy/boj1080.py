"""
3*3의 맨 왼쪽 위만 비교한다고 하면
(n - 3 + 1) * (m - 3 + 1) 칸만 행렬 B랑 똑같이 바꾼 후, 나머지 칸이 같다면 바꿀수있음, 
다르면 바꿀 수 없는연산.
왜냐면 나머지 칸이 달라서 그걸 바꾸려 들면 (n - 3 + 1) * (m - 3 + 1) 칸의 행렬이 바뀌기 
때문에 영원히 다른 행렬이 될 뿐임


"""

import sys


def change(i, j):
    for x in range(3):
        for y in range(3):
            a[i + x][j + y] = 1 - a[i + x][j + y]


def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False

    return True


n, m = map(int, input().split())

a = []
b = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    a.append(row)

for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    b.append(row)

cnt = 0
for i in range(n - 3 + 1):
    for j in range(m - 3 + 1):
        if a[i][j] != b[i][j]:
            change(i, j)
            cnt += 1

if check(): print(cnt)
else: print(-1)
