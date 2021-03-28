from sys import stdin
from collections import deque
from collections import defaultdict


def dfs(graph, start):
    stack = deque()
    visited = set()
    
    stack.append(start)
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.add(now)
            stack += graph[now] - visited

    return len(visited) - 1  # 시작점은 빼준다


graph = defaultdict(set)
computer_num = int(input())
linked_num = int(input())
for i in range(linked_num):
    computer1, computer2 = map(int, stdin.readline().split())
    graph[computer1].add(computer2)
    graph[computer2].add(computer1)

print(dfs(graph, 1))