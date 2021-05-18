from collections import defaultdict
from heapq import *
import sys

read = sys.stdin.readline


# 슈퍼컴퓨터(1) 부터 모든 컴퓨터까지의 최소 비용이므로 다익스트라 알고리즘 사용
def dijkstra(node):
    path = [0] * (N + 1)
    costs[node] = 0
    queue = [(0, node)]
    path[node] = node

    while queue:
        cost, node = heappop(queue)

        if cost > costs[node]:
            continue

        for next_node, next_cost in network[node]:
            next_cost += cost
            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                heappush(queue, (next_cost, next_node))
                path[next_node] = node
    
    return path


N, M = map(int, read().split())
network = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, read().split())
    network[A].append((B, C))
    network[B].append((A, C))

costs = [float('inf')] * (N + 1)
path = dijkstra(1)

print(N - 1)
for computer in range(2, N + 1):
    print(computer, path[computer])