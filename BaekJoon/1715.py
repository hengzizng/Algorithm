from heapq import heappop, heappush, heapify
import sys
read = sys.stdin.readline

# N: 카드 묶음 수
N = int(read())
# 카드 묶음 각각의 크기
cards = [int(read()) for _ in range(N)]
heapify(cards)

# 비교 횟수
count = 0
while True:
    card1 = heappop(cards)
    # 방금 카드 묶음이 마지막 카드 묶음이었다면 종료
    if not cards:
        break
    card2 = heappop(cards)
    count += card1 + card2
    heappush(cards, card1 + card2)

print(count)
