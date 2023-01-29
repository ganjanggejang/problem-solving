"""
테이블 정의하기
d[i] = d[i-1] + numbers[i] 와 numbers[i] 중 더 큰 값

점화식 찾기
*앞에 있는 수와 연속이 되거나, 새로운 연속합의 시작이 되거나*
d[i] = max(numbers[i] + d[i-1], numbers[i])

초기값 설정하기
d[0] = numbers[0]

"""
n = int(input())
numbers = list(map(int, input().split()))

d = [0] * n
d[0] = numbers[0]

for i in range(1, n):
    d[i] = max(numbers[i], numbers[i] + d[i - 1])

print(max(d))
