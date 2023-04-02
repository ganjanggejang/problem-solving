"""
테이블 정의하기
d[n][k] = 길이가 n인 오르막 수의 개수, k는 길이가 n-1인 오르막 수의 마지막 숫자

점화식 찾기
d[i][k] = sum(d[i-1][j]) (단, 0 <= j <= k)


초기값 설정하기
d[0][0] = 1

"""

n = int(input())

mod = 10007
d = [[0] * 10 for _ in range(n + 1)]
d[0][0] = 1

for i in range(1, n + 1):
    for k in range(10):
        for j in range(0, k + 1):
            d[i][k] += d[i - 1][j]

        d[i][k] %= mod

print(sum(d[n]) % mod)
