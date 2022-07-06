import sys
read = sys.stdin.readline


def find(target):
    while parent[target] != target:
        parent[target] = parent[parent[target]]
        target = parent[target]
    return target


def union(id1, id2):
    id1 = find(id1)
    id2 = find(id2)

    if id1 == id2:
        return count[id1]

    parent[id2] = id1
    count[id1] += count[id2]
    count[id2] = 0

    return count[id1]


T = int(read())  # 테스트 케이스 수
for _ in range(T):
    F = int(read())  # 친구 관계의 수
    parent = {}
    count = {}

    for _ in range(F):
        id1, id2 = read().strip().split(" ")
        if id1 not in parent:
            parent[id1] = id1
            count[id1] = 1
        if id2 not in parent:
            parent[id2] = id2
            count[id2] = 1

        print(union(id1, id2))
