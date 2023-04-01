import sys
read = sys.stdin.readline


def find(target):
    while parents[target] != target:
        parents[target] = parents[parents[target]]
        target = parents[target]
    return target


def union(a, b):
    a = find(a)
    b = find(b)
    parents[b] = a


N = int(read())

parents = [i for i in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, read().split())
    parents[a] = b

for a in range(N):
    parents[a] = find(a)

if len(set(parents)) == 1:
    print(parents[0] + 1)
else:
    print(-1)
