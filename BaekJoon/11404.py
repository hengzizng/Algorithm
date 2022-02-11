from sys import stdin


# n: 도시 수
n = int(input())
# m: 버스 수
m = int(input())
# 초기값 100001으로 두면 오류발생 가능함 -> inf로 두는 것이 안전
costs = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
# a: 출발 도시, b: 도착 도시, c: 비용
for _ in range(m):
    a, b, c = map(int, stdin.readline().strip().split())
    costs[a][b] = min(c, costs[a][b])

for stopover in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                costs[a][b] = 0
            else:
                costs[a][b] = min(costs[a][b],
                                  costs[a][stopover] + costs[stopover][b])

for row in range(1, len(costs)):
    for col in range(1, len(costs[0])):
        if costs[row][col] == float('inf'):
            print(0, end=' ')
        else:
            print(costs[row][col], end=' ')
    print()
