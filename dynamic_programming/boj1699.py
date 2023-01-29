"""
테이블 정의하기
d[n] = n을 제곱수의 합으로 표현할 때 그 항의 최소개수

점화식 찾기
n = i*i + (n - i*i) 로 나눌 수 있음

therefore 
d[n] = min(d[n - i*i]) + 1 (단, 1 <= i*i <= n)


초기값 설정하기
d[1] = 1

"""
n = int(input())
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = i
    j = 1
    while j * j <= i:
        d[i] = min(d[i - j * j] + 1, d[i])
        j += 1

print(d[n])
