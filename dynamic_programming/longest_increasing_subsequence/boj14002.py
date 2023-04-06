n = int(input())
arr = list(map(int, input().split()))
length = [1] * len(arr)

for k in range(1, len(arr)):
	for i in range(k):
		if arr[i] < arr[k]:
			length[k] = max(length[k], length[i] + 1)

target = max(length)
print(target)

lis = []
for i in range(len(length) - 1, -1, -1):
	if length[i] == target:
		lis.append(arr[i])
		target -= 1

lis.reverse()
for num in lis:
	print(num, end=' ')
