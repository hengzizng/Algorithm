from collections import defaultdict
from heapq import *
import sys


def dijkstra(start, is_reverse=False):
    costs = [float('inf')] * (N + 1)
    costs[start] = 0
    visited = set()

    edges = [(0, start)]
    while edges:
        cost, node = heappop(edges)
        visited.add(node)

        if cost > costs[node]:
            continue

        if is_reverse:
            for next_cost, next_node in roads_reverse[node]:
                next_cost += cost
                if next_cost < costs[next_node]:
                    heappush(edges, (next_cost, next_node))
                    costs[next_node] = next_cost
        else:
            for next_cost, next_node in roads[node]:
                next_cost += cost
                if next_cost < costs[next_node]:
                    heappush(edges, (next_cost, next_node))
                    costs[next_node] = next_cost

    return costs[1:]


read = sys.stdin.readline

# N: 학생 수, M: 도로의 수, X: 파티가 열리는 마을의 번호
N, M, X = map(int, read().split())

# roads: {출발지 : (소요시간, 도착지), ...}
roads = defaultdict(list)
# roads_reverse: {도착지 : (소요시간, 출발지), ...}
roads_reverse = defaultdict(list)
for _ in range(M):
    start, end, time = map(int, read().split())
    roads[start].append((time, end))
    roads_reverse[end].append((time, start))

to_festival = dijkstra(X, True)
to_home = dijkstra(X)

answer = 0
for i in range(N):
    answer = max(answer, to_festival[i] + to_home[i])

print(answer)
