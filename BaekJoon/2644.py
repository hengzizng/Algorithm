from collections import defaultdict
from collections import deque
from sys import stdin


def bfs(target1, target2):
    queue = deque()
    if target1 == parent[target2] or \
       target1 in relation[target2]:
        return 1

    path = 0
    visited = set()
    queue.append((target2, path))
    while queue:
        now, path = queue.popleft()
        if now == target1:
            return path
        if now not in visited:
            visited.add(now)
            queue.append((parent[now], path+1))
            for child in relation[now] - visited:
                queue.append((child, path+1))

    return -1


# n: 전체 사람의 수
# person1, person2: 촌수를 계산해야 하는 서로 다른 두 사람의 번호
# m: 부모 자식들 간의 관게의 개수
# relation: {부모: [자식1, ...]} 형태의 딕셔너리
# parent: parent[자식] = 부모 형태의 리스트
# x: y의 부모, y: x의 자식
n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
relation = defaultdict(set)
parent = [y for y in range(n + 1)]
for i in range(m):
    x, y = map(int, stdin.readline().strip().split())
    relation[x].add(y)
    parent[y] = x

print(bfs(person1, person2))
