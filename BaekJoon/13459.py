from collections import deque
import sys
read = sys.stdin.readline


# 구슬이 멈춘 위치를 반환
def move(r, c, d, else_r, else_c):
    # 현재 움직이는 구슬의 위치
    nr, nc = r, c
    # 현재 움직이는 구슬이 다른 구슬을 지나쳤는지 여부
    pass_by = False
    # 구슬이 멈출 때까지 계속 이동
    while board[nr][nc] == ".":
        nr, nc = nr + drdc[d][0], nc + drdc[d][1]
        # 현재 구슬이 다른 구슬을 지나쳤다면, 다른 구슬이 먼저 움직여야 한다.
        if nr == else_r and nc == else_c:
            pass_by = True

    # 구슬이 구멍을 만나서 멈췄다면
    if board[nr][nc] == "O":
        return -1, -1
    # 구슬이 벽을 만나서 멈췄는데 다른 구슬을 지나쳤다면
    if pass_by:
        nr, nc = nr - drdc[d][0], nc - drdc[d][1]

    return nr - drdc[d][0], nc - drdc[d][1]


def play(red_r, red_c, blue_r, blue_c):
    queue = deque([(red_r, red_c, blue_r, blue_c, 0)])
    checked = set([(red_r, red_c, blue_r, blue_c)])

    while queue:
        red_r, red_c, blue_r, blue_c, count = queue.popleft()

        for d in range(4):  # 네 방향으로 기울인다.
            # 파란 구슬 이동
            blue_nr, blue_nc = move(blue_r, blue_c, d, red_r, red_c)
            # 파란 구슬이 구멍에 빠졌다면 무조건 실패
            if blue_nr == -1:
                continue

            # 빨간 구슬 이동
            red_nr, red_nc = move(red_r, red_c, d, blue_r, blue_c)
            # 빨간 구슬만 구멍에 빠졌다면 성공
            if red_nr == -1:
                # print("(", count + 1, ")", red_r, red_c, blue_r, blue_c, " => ", red_nr, red_nc, blue_nr, blue_nc)
                return 1

            # 과거에 시도하지 않았던 위치이고, 10번 미만으로 움직였다면 계속 진행
            if (red_nr, red_nc, blue_nr, blue_nc) not in checked and count + 1 < 10:
                # print("(", count + 1, ")", red_r, red_c, blue_r, blue_c, " -> ", red_nr, red_nc, blue_nr, blue_nc)
                queue.append((red_nr, red_nc, blue_nr, blue_nc, count + 1))
                checked.add((red_nr, red_nc, blue_nr, blue_nc))

    return 0


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
N, M = map(int, read().split())  # 행 수, 열 수
board = [list(read().strip()) for _ in range(N)]

# 구슬들의 위치를 찾는다.
red_r, red_c, blue_r, blue_c = -1, -1, -1, -1
for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            red_r, red_c = r, c
            board[r][c] = "."
        elif board[r][c] == "B":
            blue_r, blue_c = r, c
            board[r][c] = "."

print(play(red_r, red_c, blue_r, blue_c))
