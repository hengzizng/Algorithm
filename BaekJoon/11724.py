from collections import defaultdict, deque
import sys
read = sys.stdin.readline


N, M = map(int, read().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, start):
    linked = 1
    left = set(range(1, N + 1))
    stack = deque([start])

    while stack:
        node = stack.pop()

        for next_node in graph[node]:
            if next_node in left:
                stack.append(next_node)
                left.remove(next_node)
        
        if not stack and left:
            linked += 1
            stack.append(left.pop())

    return linked

print(dfs(graph, v))