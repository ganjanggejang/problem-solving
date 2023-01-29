"""
결정 문제: mid시간만큼 심사를 한다면 모든 사람이 심사를 받을 수 있는가?
결정문제분포: fffftttttt

Check() 구현
각 심사대마다 mid초 동안 심사할 수 있는 사람의 총합 cnt가 m 이상인지 확인
이때 한 명당 t초가 걸리는 심사대에서 mid초 동안 심사할 수 있는 사람은 mid//time
"""


def check(mid, times, n):
    cnt = 0
    for time in times:
        cnt += mid // time

    return cnt >= n
  
def solution(n, times):
    lo = 0
    hi = max(times) * n + 1

    while lo + 1 < hi:
        mid = (lo+hi)//2
        if check(mid, times, n): hi = mid
        else: lo = mid

    return hi
