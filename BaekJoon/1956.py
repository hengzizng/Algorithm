# !! 백준 내 제출에서는 pypy3으로 제출해야 시간 초과 발생하지 않음
from sys import stdin


# V: 마을 수, E: 도로 수
V, E = map(int, input().split())
maps = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]
# a: 출발지, b: 도착지, c: a와 b 간 거리
for _ in range(E):
    a, b, c = map(int, stdin.readline().strip().split())
    maps[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            maps[i][j] = min(maps[i][j], maps[i][k]+maps[k][j])

min_distance = float('inf')
for i in range(1, V+1):
    min_distance = min(min_distance, maps[i][i])

print(-1 if min_distance == float('inf') else min_distance)
