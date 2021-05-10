from collections import defaultdict
from collections import deque

'''
# bfs를 하면서 제거된 노드 제외하고 리프노드를 만나면 카운트 증가
def dfs1(start, deleted_node):
    if start == deleted_node:
        return 0

    stack = deque([start])
    visited = set([start, deleted_node])
    count = 0

    while stack:
        node = stack.pop()

        if (
            not tree[node] or
            (len(tree[node]) == 1 and tree[node][0] == deleted_node)
        ):
            count += 1

        for next_node in tree[node]:
            if next_node not in visited:
                stack.append(next_node)
                visited.add(next_node)

    return count


# N: 노드의 개수
N = int(input())

tree = defaultdict(list)
parents = list(map(int, input().split()))
delete_node = int(input())

for node, parent in enumerate(parents):
    if parent == -1:
        start = node
    tree[parent].append(node)

print(dfs1(start, delete_node))
'''

# 지워진 노드들과 그 자식들을 먼저 제거 후 부모 리스트에 없는 노드 카운트
def dfs2(deleted_node):
    stack = deque([deleted_node])
    parents[deleted_node] = deleted_node

    while stack:
        node = stack.pop()

        for next_node in tree[node]:
            if parents[next_node] != next_node:
                stack.append(next_node)
                parents[next_node] = next_node


# N: 노드의 개수
N = int(input())

parents = list(map(int, input().split()))
delete_node = int(input())

tree = defaultdict(list)
for node, parent in enumerate(parents):
    tree[parent].append(node)

dfs2(delete_node)

parents = set(parents)
total = set(range(N))

print(len(total - parents))