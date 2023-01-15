import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)  # 최소 힙

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards, x + y)

sum = 0
for card in cards:
    sum += card

print(sum)
