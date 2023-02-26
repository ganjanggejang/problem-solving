def lower_idx(len, target):
    lo = -1
    hi = len
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if input_list[mid] >= target: hi = mid
        else: lo = mid

    return hi


n = int(input())
input_list = list(map(int, input().split()))
input_list.sort()
m = int(input())
target_list = list(map(int, input().split()))

for target in target_list:
    x = lower_idx(n, target)
    if not (0 <= x < n):
        print(0, end=' ')
    else:
        if input_list[lower_idx(n, target)] == target:
            print(1, end=' ')
        else:
            print(0, end=' ')
