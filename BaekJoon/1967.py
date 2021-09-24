from collections import defaultdict, deque
import sys
sys.stdin = open("TestCase/BaekJoon/1967input.txt", "r")
read = sys.stdin.readline


def dfs(node):
    stack = deque()
    visited = set()

    stack.append((node, 0))
    visited.add(node)

    while stack:
        node, weight = stack.pop()
        if weight > diameter[1]:
            diameter[0] = node
            diameter[1] = weight
        
        for next_weight, next_node in linked[node]:
            if next_node not in visited:
                visited.add(next_node)
                stack.append((next_node, weight + next_weight))


n = int(read()) # 노드의 개수
linked = defaultdict(list)
for _ in range(n - 1):
    parent, child, weight = map(int, read().split())
    linked[parent].append((weight, child))
    linked[child].append((weight, parent))

diameter = [-1, 0] # 지름의 한쪽 끝 노드 번호, 지름의 길이
dfs(1)
dfs(diameter[0])

print(diameter[1])
