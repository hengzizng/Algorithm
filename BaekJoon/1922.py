from collections import defaultdict
from sys import stdin


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)
    

# N: 컴퓨터의 수
N = int(input())
# M: 연결할 수 있는 선의 수
M = int(input())

parent = list(range(N+1))
connections = []
# a, b: 컴퓨터, c: a와 b를 연결하는 데 드는 비용
for _ in range(M):
    a, b, c = map(int, stdin.readline().strip().split())
    connections.append((c, a, b))
connections.sort()

total_price = 0
for price, a, b in connections:
    if find(a) != find(b):
        union(a, b)
        total_price += price

print(total_price)