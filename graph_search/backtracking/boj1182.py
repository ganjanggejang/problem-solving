n, s = map(int, input().split())

numbers = list(map(int, input().split()))
is_used = [False] * len(numbers)  # true or false, len(numbers) == n
count = 0


def backtracking(k, sum):
    if k == len(numbers):  # base condition
        if sum == s:
            global count
            count += 1
        return

    if not is_used[k]:
        is_used[k] = True
        backtracking(k + 1, sum + numbers[k])
        backtracking(k + 1, sum)
        is_used[k] = False


backtracking(0, 0)
if s == 0 and count > 0:
    print(count - 1)
else:
    print(count)
