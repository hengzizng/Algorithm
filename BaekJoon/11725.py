from collections import deque
import sys
read = sys.stdin.readline


N = int(read())

linked = {}
for node in range(1, N + 1):
    linked[node] = []

for _ in range(N - 1):
    node1, node2 = map(int, read().split())
    linked[node1].append(node2)
    linked[node2].append(node1)

parents = list(range(N + 1))
queue = deque([1])
visited = set([1])
while queue:
    node = queue.popleft()
    for next_node in linked[node]:
        if next_node not in visited:
            parents[next_node] = node
            queue.append(next_node)
            visited.add(next_node)

for i in range(2, N + 1):
    print(parents[i])
