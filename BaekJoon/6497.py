from collections import defaultdict
from heapq import *
from sys import stdin


def prim(m, graph):
    distances = [float('inf') for _ in range(m)]
    distances[0] = 0
    for distance, destination in graph[0]:
        distances[destination] = distance

    connected = set([0])
    candidate_edges = graph[0]
    heapify(candidate_edges)

    while candidate_edges:
        distance, destination = heappop(candidate_edges)
        if destination not in connected:
            connected.add(destination)
            distances[destination] = min(distances[destination], distance)
            for edge in graph[destination]:
                heappush(candidate_edges, edge)

    return sum(distances)


answers = []
# m: 집의 수, n: 길의 수
m, n = map(int, input().split())
while m != 0 and n != 0:
    graph = defaultdict(list)
    total_distance = 0
    # x, y: 집, z: x와 y 사의의 거리
    for _ in range(n):
        x, y, z = map(int, stdin.readline().strip().split())
        graph[x].append((z, y))
        graph[y].append((z, x))
        total_distance += z

    answers.append(total_distance - prim(m, graph))
    m, n = map(int, input().split())

for answer in answers:
    print(answer)