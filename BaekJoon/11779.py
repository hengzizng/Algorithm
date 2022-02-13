from collections import defaultdict
from heapq import *
import sys

read = sys.stdin.readline


def dijkstra(start):
    path = list(range(n + 1))
    costs[start] = 0
    nodes = [(0, start)]

    while nodes:
        cost, node = heappop(nodes)

        if cost > costs[node]:
            continue

        for next_node, next_cost in route[node]:
            # costs[node]가 아닌 cost를 더해준다 (위 조건절에 의해 cost가 더 작다)
            next_cost += cost
            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                path[next_node] = node
                heappush(nodes, (next_cost, next_node))

    return path


# n: 도시의 수
n = int(read())
# m: 버스의 수
m = int(read())
route = defaultdict(list)
for _ in range(m):
    departure, destination, cost = map(int, read().split())
    route[departure].append((destination, cost))
departure, destination = map(int, read().split())

costs = [float('inf')] * (n + 1)
path = dijkstra(departure)

node = destination
min_distance_path = [node]
while node != path[node]:
    node = path[node]
    min_distance_path.append(node)

print(costs[destination])
print(len(min_distance_path))
print(' '.join(map(str, min_distance_path[::-1])))
