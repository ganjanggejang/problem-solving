import sys

n = int(input())
wire = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    wire.append([a, b])

wire.sort()
arr = []
for a, b in wire:
    arr.append(b)

# LIS 구하는 부분 boj11053 코드와 같음
length = [1] * len(arr)

for k in range(1, len(arr)):
    for i in range(k):
        if arr[i] < arr[k]:
            length[k] = max(length[k], length[i] + 1)

print(len(arr) - max(length))
