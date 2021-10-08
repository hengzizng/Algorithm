'''
# 첫 번째 풀이 > 다익스트라 사용
# 테스트 1 〉	통과 (0.03ms, 10.1MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.55ms, 10.3MB)
# 테스트 5 〉	통과 (1.83ms, 10.6MB)
# 테스트 6 〉	통과 (3.95ms, 11.7MB)
# 테스트 7 〉	통과 (44.57ms, 22.2MB)
# 테스트 8 〉	통과 (57.86ms, 27.2MB)
# 테스트 9 〉	통과 (72.11ms, 27.3MB)
from heapq import *
from collections import defaultdict


def solution(n, vertex):
    def dijkstra(start):
        edges = [(0, start)]
        distance = [float('inf')] * (n + 1)
        distance[start] = 0
        
        while edges:
            cost, node = heappop(edges)
            
            if cost > distance[node]:
                continue
            
            for next_node, next_cost in graph[node]:
                next_cost += cost
                
                if next_cost < distance[next_node]:
                    distance[next_node] = next_cost
                    heappush(edges, (next_cost, next_node))
        
        return distance[1:]
        
    
    graph = defaultdict(list)
    for vertex1, vertex2 in vertex:
        graph[vertex1].append((vertex2, 1))
        graph[vertex2].append((vertex1, 1))
    
    distance = dijkstra(1)
    
    return distance.count(max(distance))
'''

# 두 번째 풀이 > BFS 사용
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.32ms, 10.3MB)
# 테스트 5 〉	통과 (0.75ms, 10.5MB)
# 테스트 6 〉	통과 (2.15ms, 11MB)
# 테스트 7 〉	통과 (24.01ms, 18.4MB)
# 테스트 8 〉	통과 (33.02ms, 23.7MB)
# 테스트 9 〉	통과 (40.23ms, 23.8MB)
from collections import defaultdict, deque


def solution(n, vertex):
    graph = defaultdict(list)

    for node_a, node_b in vertex:
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    queue = deque([(1, 0)])
    visited = set([1])
    distances = defaultdict(list)

    while queue:
        node, distance = queue.popleft()
        distances[distance].append(node)

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, distance + 1))
    
    max_distance = max(distances.keys())

    return len(distances[max_distance])


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex), 3)