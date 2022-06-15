import sys
sys.stdin = open("TestCase/BaekJoon/15591input.txt")
read = sys.stdin.readline


def find(target):
    while target != parent[target]:
        parent[target] = parent[parent[target]]
        target = parent[target]
    return target


def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)


N, Q = map(int, read().split())  # 동영상 수, 질문 수
usado = []  # [(유사도, 동영상1, 동영상2)]
for _ in range(N - 1):
    p, q, r = map(int, read().split())
    usado.append((r, p, q))
# 유사도 내림차순으로 정렬
usado.sort(reverse=True)

limit = []
origin = []
for index in range(Q):
    k, v = map(int, read().split())
    limit.append((k, index))
    origin.append(v)
limit.sort()

parent = list(range(N + 1))
parent_value = [1] * (N + 1)
result = [0] * Q

i = 0
while limit:
    limit_now, limit_index = limit.pop()

    while i <= N - 2 and usado[i][0] >= limit_now:
        p, q = usado[i][1], usado[i][2]
        total = parent_value[find(p)] + parent_value[find(q)]

        union(p, q)
        parent_value[find(p)] = total
        i += 1

    result[limit_index] = parent_value[find(origin[limit_index])] - 1
print(parent, parent_value)
print(*result, sep='\n')
