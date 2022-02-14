from collections import deque, defaultdict
import sys
read = sys.stdin.readline


def bfs(node, graph):
    queue = deque()
    visited = [False for _ in range(N + 1)]

    queue.append(node)
    visited[node] = True
    count = 1

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                count += 1

    return count


N, M = map(int, read().split(" "))
graph = defaultdict(list)
for _ in range(M):
    to_node, from_node = map(int, read().split(" "))
    graph[from_node].append(to_node)

max_count = 0
max_count_nodes = []
for n in range(1, N + 1):
    temp = bfs(n, graph)
    if max_count == temp:
        max_count_nodes.append(n)
    elif max_count < temp:
        max_count = temp
        max_count_nodes.clear()
        max_count_nodes.append(n)

print(*max_count_nodes)
