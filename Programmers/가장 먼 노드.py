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