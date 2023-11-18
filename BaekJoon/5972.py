from collections import defaultdict
from heapq import *
import sys
read = sys.stdin.readline


# N: 헛간의 수, M: 길의 수
N, M = map(int, read().split())
# roads[i]: [(헛간 i에서 j로 이동하는데 필요한 비용(소의 수), j), ...]
roads = defaultdict(list)
# 출발지 - 각 index 까지 최소 비용
costs = [float('inf')] * N
for _ in range(M):
    A, B, C = map(int, read().split())
    roads[A - 1].append((C, B - 1))
    roads[B - 1].append((C, A - 1))

# pq: 우선순위 큐
# (헛간 i까지의 최소비용, 헛간 i)
pq = [(0, 0)]
while pq:
    cost, node = heappop(pq)
    
    if cost > costs[node]:
        continue

    for next_cost, next_node in roads[node]:
        new_cost = cost + next_cost
        if new_cost < costs[next_node]:
            costs[next_node] = new_cost
            heappush(pq, (new_cost, next_node))

print(costs[N - 1])
