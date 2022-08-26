import sys
read = sys.stdin.readline


# 공의 수 (최대 색상 개수)
N = int(read())
# counts[size][color]: size 크기이고 color 색인 공의 수
counts = [[0] * (N + 2) for _ in range(2001)]

balls = []
for _ in range(N):
    c, s = map(int, read().split())
    counts[s][c] += 1
    balls.append((c, s))

# counts[size][color]: size 크기 이하인 color 색 공들 크기의 합
# counts[size][N + 1]: size 크기 이하 모든 색 공들 크기의 합
for size in range(1, 2001):
    for color in range(N + 1):
        counts[size][color] = counts[size - 1][color] + counts[size][color] * size
        counts[size][N + 1] += counts[size][color]

for c, s in balls:
    # 크기가 s보다 1 작은 공들 크기의 합에서 같은 색상만 제외
    print(counts[s - 1][N + 1] - counts[s - 1][c])
