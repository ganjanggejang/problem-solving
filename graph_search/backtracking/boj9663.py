n = int(input())

count = 0
row = [0] * n
"""
[x][y] 2차원 배열이라고 생각하면, [k][i]에 퀸을 놓음
row = 
[
0,
0,
0,
...
]

"""


# 퀸을 놓을 수 있는지 확인하는 함수
def is_queen_ok(k):
    for t in range(k):
        # 이미 같은 열에 퀸이 있거나, 이미 대각선에 퀸이 있으면 False 출력
        if row[k] == row[t] or abs(row[k] - row[t]) == abs(k - t):
            return False

    return True


# 퀸을 놓는 함수
def backtracking(k):
    global count
    if k == n:
        count += 1
        return
    else:
        for i in range(n):
            row[k] = i  # [x][y] 2차원 배열이라고 생각하면, [k][i]에 퀸을 놓음
            if is_queen_ok(k):
                backtracking(k + 1)


backtracking(0)
print(count)
