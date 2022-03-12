# 40 min

from collections import deque
import sys
read = sys.stdin.readline


# 구름을 d방향으로 s만큼 이동하고, 비가 내린다.
def move_cloud(d, s, cloud, can_cloud):
    for _ in range(len(cloud)):
        r, c = cloud.popleft()

        # 구름 이동
        r = (r + (s * dr[d])) % N
        c = (c + (s * dc[d])) % N
        # # 구름 이동 (음수일경우 생각)
        # r = (r + (s * ((N + dr[d]) if dr[d] < 0 else dr[d]))) % N
        # c = (c + (s * ((N + dc[d]) if dc[d] < 0 else dc[d]))) % N

        # 비가 내린다.
        water[r][c] += 1
        can_cloud[r][c] = False

        # 이동한 곳의 위치를 다시 저장해둔다
        cloud.append((r, c))


# 물복사버그 마법
def magic(cloud):
    while cloud:
        r, c = cloud.popleft()
        amount = 0  # 증가할 양 (물이 있는 대각 방향 수)
        for i in range(1, 8, 2):  # 대각선만 확인
            nr, nc = dr[i] + r, dc[i] + c
            if 0 <= nr < N and 0 <= nc < N and water[nr][nc] > 0:
                amount += 1
        water[r][c] += amount  # 물 증가


# 구름을 만든다
def make_cloud(cloud, can_cloud):
    for r in range(N):
        for c in range(N):
            if can_cloud[r][c] and water[r][c] >= 2:
                cloud.append((r, c))
                water[r][c] -= 2
            can_cloud[r][c] = True


# 0: ←, 1: ↖, 2: ↑, 3: ↗, 4: →, 5:↘, 6: ↓, 7: ↙
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# N: 격자 크기, M: 이동 횟수, water: 각 칸마다 바구니에 담긴 물의 양
N, M = map(int, read().split())
water = [list(map(int, read().split())) for _ in range(N)]

can_cloud = [[True] * N for _ in range(N)]  # 구름이 생길 수 있는지 여부
cloud = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])  # 구름
for _ in range(M):  # M번 이동
    d, s = map(int, read().split())  # d: 방향, s: 거리
    move_cloud(d - 1, s, cloud, can_cloud)  # 구름 이동, 비내림
    magic(cloud)  # 물복사버그 마법
    make_cloud(cloud, can_cloud)  # 구름을 만든다

# 물의 양의 합 출력
water_sum = 0
for row in water:
    water_sum += sum(row)
print(water_sum)
