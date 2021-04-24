from sys import stdin
from collections import defaultdict
from heapq import *


def dijkstra(start, end):
    edges = []
    costs = [float('inf')] * (N + 1)
    heappush(edges, (0, start))
    costs[start] = 0

    while edges:
        cost, city = heappop(edges)

        if costs[city] < cost:
            continue
        
        for next_cost, next_city in cities[city]:
            next_cost += costs[city]
            if next_cost < costs[next_city]:
                costs[next_city] = next_cost
                heappush(edges, (next_cost, next_city))
    
    return costs[end]


# N: 도시의 수
N = int(input())
# M: 버스의 수
M = int(input())
cities = defaultdict(list)
for _ in range(M):
    departure, destination, cost = map(int, stdin.readline().split())
    cities[departure].append((cost, destination))

departure, destination = map(int, input().split())
print(dijkstra(departure, destination))