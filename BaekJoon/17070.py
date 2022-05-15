import sys
read = sys.stdin.readline


N = int(read())  # 집의 크기
house = [list(map(int, read().split())) for _ in range(N)]  # 0: 빈 칸, 1: 벽

# 각 위치별로 파이프가 올 수 있는 방법의 수 (행, 열, 방향(0: →, 1: ↓, 2: ↘))
way_count = [[[0] * 3 for _ in range(N + 1)] for _ in range(N + 1)]
way_count[1][2][0] = 1

for r in range(1, N + 1):  # 현재 행
    for c in range(1, N + 1):  # 현재 열
        if (r == 1 and c <= 2) or house[r - 1][c - 1] == 1:
            continue
        # →
        way_count[r][c][0] = way_count[r][c - 1][0] + way_count[r][c - 1][2]
        # ↓
        way_count[r][c][1] = way_count[r - 1][c][1] + way_count[r - 1][c][2]
        # ↘
        if house[r - 2][c - 1] == 0 and house[r - 1][c - 2] == 0:
            way_count[r][c][2] = sum(way_count[r - 1][c - 1])

print(sum(way_count[N][N]))
