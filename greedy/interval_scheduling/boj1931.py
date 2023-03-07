import sys

n = int(input())

meeting = []
for _ in range(n):
    st, en = map(int, sys.stdin.readline().split())
    meeting.append((st, en))

meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 1
now = meeting[0][1]  # now = en
for i in range(1, n):
    if meeting[i][0] >= now:  # st >= now
        cnt += 1
        now = meeting[i][1]  # now = en

print(cnt)
