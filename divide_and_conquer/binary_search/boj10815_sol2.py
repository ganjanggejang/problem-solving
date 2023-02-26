from bisect import bisect_left

n = int(input())
input_list = list(map(int, input().split()))
input_list.sort()
m = int(input())
target_list = list(map(int, input().split()))

for target in target_list:
    x = bisect_left(input_list, target)
    if not (0 <= x < n):
        print(0, end=' ')
    else:
        if input_list[x] == target:
            print(1, end=' ')
        else:
            print(0, end=' ')
