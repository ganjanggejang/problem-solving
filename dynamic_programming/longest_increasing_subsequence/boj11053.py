n = int(input())
arr = list(map(int, input().split()))
length = [1] * len(arr)

for k in range(1, len(arr)):
    for i in range(k):
        if arr[i] < arr[k]:
            length[k] = max(length[k], length[i] + 1)

print(max(length))
