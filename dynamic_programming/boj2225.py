"""
1, 2, 3 더하기 : n을 1, 2, 3의 합으로 표현
합분해: n을 0, 1, 2, ... n 중 k개의 합으로 표현

"""
"""
테이블 정의하기
d[k][n] = 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수

점화식 찾기
n = x + (n-x)로 나타낼 수 있음
n-x의 합은 정수 k-1개를 더해서 나온 값임

d[k][n] = sum(d[k-1][n-x]) (단, 0 <= x <= n)



초기값 설정하기
d[0][0] = 1

"""
n, k = map(int, input().split())
mod = 1000000000
d = [[0] * (n + 1) for _ in range(k + 1)]
d[0][0] = 1

for k_seq in range(1, k + 1):
    for n_seq in range(0, n + 1):
        for x in range(0, n_seq + 1):
            d[k_seq][n_seq] += d[k_seq - 1][n_seq - x]
            d[k_seq][n_seq] %= mod

print(d[k][n])
