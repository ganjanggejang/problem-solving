import sys

n = int(input())
matrix = []
cnt = [0, 0, 0]  # -1, 0, 1로 이루어진 '종이'의 개수, 순서대로 0, 1, 2번째 index에 저장

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)


def solve(x, y, n):
    if same(x, y, n):
        cnt[matrix[x][y] + 1] += 1
        return

    # x, y부터 x+n, y+n까지 같지 않은게 하나 이상 있다면, 9등분 분할하여 각각의 조각에 대해 solve()
    m = n // 3
    for i in range(3):
        for j in range(3):
            solve(x + i * m, y + j * m, m)


def same(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[x][y] != matrix[i][j]:
                return False

    return True


solve(0, 0, n)
for ans in cnt:
    print(ans)
