n, m = map(int, input().split())

arr = [0] * (m + 1)  # 수열을 담을 list, 1-based indexing
is_used = [False] * (n + 1)  # true or false, 1-based indexing


# k번째 함수 프레임(call stack)이 arr[k]에 들어갈 숫자를 결정
# 따라서 print(arr)이 실행될 땐 k == 1부터 k == m+1 까지 m+1개의 함수 프레임이 살아있는 상태
def backtracking(k):
    if k == m + 1:  # base condition 재귀 종료 조건
        for i in range(1, len(arr)):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            backtracking(k + 1)
            is_used[i] = False


backtracking(1)
