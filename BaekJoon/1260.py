from collections import defaultdict
from collections import deque
from sys import stdin
# import pprint


# pp = pprint.PrettyPrinter(indent=4)


def dfs(graph, start) -> int:
    stack = deque()

    visited = []
    stack.append(start)
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack += [node for node in graph[now] if node not in visited]

    return visited

def bfs(graph, start) -> int:
    queue = deque()
    
    visited = []
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            queue += [node for node in graph[now] if node not in visited]

    return visited


# N:정점 개수, M:간선 개수, V:탐색 시작 노드번호
N, M, V = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    node1, node2 = map(int, stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


for key in graph.keys():
    graph[key].sort(reverse = True)
for result in dfs(graph, V):
    print(result, end=' ')

print()

for key in graph.keys():
    graph[key].sort()
for result in bfs(graph, V):
    print(result, end=' ')
