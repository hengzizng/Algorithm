import sys
read = sys.stdin.readline


# 경로를 모두 저장할 필요 없이 방향만 저장해두면 구현이 간단해진다.

# 이전 세대를 시계 방향으로 90도 회전시킨 후 이전 세대의 끝점에 붙이면,
# 이전 세대 끝점 -> 이번 세대 끝점 경로의 이동 방향은
#   시작점 -> 이전 세대 끝점 경로의 이동 방향을
#   각각 반시계 방향으로 90도 회전시키고 순서를 반대로 바꾼 것과 같다.
# 예시의 2세대 드래곤 커브 이동 방향 : 우(~) 상(!) 좌(!) 상(~)
# 예시의 3세대 드래곤 커브 이동 방향 : 우(~) 상(!) 좌(@) 상(#) 좌(#) 하(@) 좌(!) 상(~)


drdc = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # →(0) ↑(1) ←(2) ↓(3) 방향 벡터
axis = [[0] * 101 for _ in range(101)]  # 격자 상태 (1: 드래곤 커브 존재)
N = int(read())  # 드래곤 커브의 개수
for _ in range(N):
    # (x, y): 시작점, d: 방향, g: 세대
    x, y, d, g = map(int, read().split())
    # 이동 방향들을 저장
    directions = [d]
    for _ in range(g):
        for i in range(len(directions) - 1, 0 - 1, -1):
            directions.append((directions[i] + 1) % 4)

    # 시작점 격자에 표시 (y가 행, x가 열 !주의!)
    axis[y][x] = 1
    # 방향대로 이동하며 격자에 표시
    for d in directions:
        y, x = y + drdc[d][0], x + drdc[d][1]
        axis[y][x] = 1

# 네 꼭짓점이 모두 드래곤 커브의 일부인 칸의 개수
count = 0
for r in range(100):
    for c in range(100):
        if axis[r][c] == 1 and axis[r + 1][c] == 1 and axis[r][c + 1] == 1 and axis[r + 1][c + 1] == 1:
            count += 1

print(count)
