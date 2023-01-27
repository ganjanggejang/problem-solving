"""
테이블 정의하기
d[i] = 카드 i개를 샀을 때 금액의 최댓값

점화식 찾기
카드 총 i개 중의 모든 카드팩 중 
하나의 카드팩엔 k개, 나머지 카드팩엔 i-k개가 있을 것

i-k개를 잘 구매한 뒤, k개를 구매해주면 되므로
모든 1부터 i까지의 k들 중 d[i-k] + p[k]가 최대가 되는 k에서 d[i]가 나옴

d[i] = max(d[i-k] + p[k]), k는 1부터 i까지
therefore d[i] = max(d[i-k] + p[k], d[i])

초기값 설정하기
d[1] = p[1]

"""
n = int(input())
temp = [0]
p = list(map(int, input().split()))
p = temp + p  # 1-based

d = [0] * (n + 1)

d[1] = p[1]

for i in range(2, n + 1):
    for k in range(1, i + 1):
        d[i] = max(d[i - k] + p[k], d[i])

print(d[n])
