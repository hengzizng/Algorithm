from collections import deque
from heapq import *
import sys
read = sys.stdin.readline


def delete_path(start, destination, target_distance):
    queue = deque([(destination, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == start:
            continue

        for before_node in range(N):
            before_distance = map_matrix[before_node][node]
            
            if before_distance == 0:
                continue

            before_distance += distance
            if before_distance + distances[before_node] == target_distance:
                queue.append((before_node, before_distance))
                map_matrix[before_node][node] = 0


def get_min_distance(start, destination):
    edges = [(0, start)]
    distances[start] = 0
    
    while edges:
        distance, node = heappop(edges)

        if distance > distances[node]:
            continue

        for next_node, next_distance in enumerate(map_matrix[node]):
            if next_distance == 0:
                continue

            next_distance += distance
            if next_distance < distances[next_node]:
                heappush(edges, (next_distance, next_node))
                distances[next_node] = next_distance

    return distances[destination]


answers = []
# N: 장소의 수, M: 도로의 수
N, M = map(int, read().split())
while N > 0 and M > 0:
    # map_matrix : 도로 정보를 행렬 형태에 저장
    map_matrix = [[0] * N for _ in range(N)]
    # S: 시작점, D: 도착점
    S, D = map(int, read().split())

    for _ in range(M):
        U, V, P = map(int, read().split())
        map_matrix[U][V] = P

    distances = [float('inf')] * N
    min_distance = get_min_distance(S, D)
    delete_path(S, D, min_distance)
    
    distances = [float('inf')] * N
    answers.append(get_min_distance(S, D))

    N, M = map(int, read().split())


for answer in answers:
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)