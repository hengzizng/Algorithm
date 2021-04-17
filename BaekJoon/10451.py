from sys import stdin
from collections import deque


def dfs(graph, node, visited):
    stack = deque([node])
    visited[node] = True

    while stack:
        now_node = stack.pop()
        
        next_node = graph[now_node]
        if visited[next_node]:
            break
        else:
            stack.append(next_node)
            visited[next_node] = True


# T: 테스트 케이스의 개수
T = int(input())
answer = [0 for _ in range(T)]
for test in range(T):
    # N: 순열의 크기
    N = int(stdin.readline().strip())
    numbers = list(map(int, stdin.readline().split()))
    linked_info = {}
    for departure, destination in enumerate(numbers, 1):
        linked_info[departure] = destination
    
    visited = [False for _ in range(N+1)]
    for node in range(1, N+1):
        if not visited[node]:
            dfs(linked_info, node, visited)
            answer[test] += 1

for count in answer:
    print(count)