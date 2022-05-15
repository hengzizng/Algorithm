import sys
read = sys.stdin.readline


def is_valid(r, c):
    if r < 0 or r >= N or c < 0 or c >= N or house[r][c] == 1:
        return False
    return True


# 0: →, 1: ↓, 2: ↘
drdc = [[0, 1], [1, 0], [1, 1]]
# 이동 가능한 방향 리스트
move_direction = [[0, 2], [1, 2], [0, 1, 2]]

N = int(read())  # 집의 크기
house = [list(map(int, read().split())) for _ in range(N)]  # 0: 빈 칸, 1: 벽

# 각 위치별로 파이프가 올 수 있는 방법의 수 (행, 열, 방향)
way_count = [[[0] * 3 for _ in range(N)] for _ in range(N)]
way_count[0][1][0] = 1

for r in range(N):  # 현재 행
    for c in range(1, N):  # 현재 열
        for d in range(3):  # 현재 방향
            for nd in move_direction[d]:  # 이동할 방향
                nr, nc = r + drdc[nd][0], c + drdc[nd][1]  # 이동할 위치
                if not is_valid(nr, nc):
                    continue

                can_move = True
                if nd == 2:  # 만약 이동할 방향이 대각선이라면 나머지 두 방향도 확인
                    for temp_d in range(2):
                        if not is_valid(r + drdc[temp_d][0], c + drdc[temp_d][1]):
                            can_move = False
                            break

                if can_move:
                    way_count[nr][nc][nd] += way_count[r][c][d]

print(sum(way_count[N - 1][N - 1]))
