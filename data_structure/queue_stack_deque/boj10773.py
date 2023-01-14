import sys

k = int(input())
stack = []

for _ in range(k):
    num = int(sys.stdin.readline())

    if num == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack.append(num)

sum = 0
for n in stack:
    sum += n

print(sum)
