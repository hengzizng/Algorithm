import sys
read = sys.stdin.readline


def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)

    parents[max(node1, node2)] = min(node1, node2)


def find(target):
    while target != parents[target]:
        parents[target] = parents[parents[target]]
        target = parents[target]

    return target


N, M = map(int, read().split())
parents = list(range(N + 1))
for _ in range(M):
    u, v = map(int, read().split())
    union(u, v)

parents_set = set()
for node in range(1, N + 1):
    parents[node] = find(node)
    parents_set.add(parents[node])

print(len(parents_set))
