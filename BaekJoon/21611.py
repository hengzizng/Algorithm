# 80 min

from collections import deque
import sys
read = sys.stdin.readline


# (r, c)가 격자 내의 위치인지 판단(유효여부 판단)
def is_valid(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    else:
        return False


# d 방향으로 거리가 s 이하인 모든 칸의 구슬을 파괴
def destroy(d, s):
    d = d_map[d]
    nr, nc = mid_N, mid_N
    for _ in range(s):
        nr, nc = nr + drdc[d][0], nc + drdc[d][1]
        board[nr][nc] = 0


# 4개 이상 연속하는 구슬 폭발
def explode(balls):
    is_explode = True
    while is_explode:  # 구슬이 폭발한적 없을때까지 반복
        is_explode = False
        new_balls = deque()
        while balls:  # 모든 구슬 반복
            ball = balls.popleft()
            if ball[1] < 4:  # 구슬이 4개 미만일 때만 다시 넣어준다.
                if new_balls and new_balls[-1][0] == ball[0]:
                    new_balls[-1][1] += ball[1]
                else:
                    new_balls.append(ball)
            else:  # 구슬이 4개 이상이어서 폭발했다면
                is_explode = True
                explode_count[ball[0]] += ball[1]
        balls = new_balls

    return new_balls


# 2차원 배열 board에서 [구슬 번호, 개수] 로 이루어진 deque를 반환
def get_balls():
    balls = deque()
    r, c, d = mid_N, mid_N, -1

    size = 0  # 나선의 한 변 크기
    while True:
        size += 1
        for _ in range(2):
            d = (d + 1) % 4
            for _ in range(size):
                nr, nc = r + drdc[d][0], c + drdc[d][1]
                if not is_valid(nr, nc):
                    return balls

                r, c = nr, nc
                ball_no = board[nr][nc]
                if ball_no == 0:  # 비어있는 칸은 구슬이 아님
                    continue

                if balls and balls[-1][0] == ball_no:
                    balls[-1][1] += 1
                else:
                    balls.append([ball_no, 1])


# [구슬 번호, 개수] 로 이루어진 deque를 board에 옮긴다.
def set_balls(balls):
    if not balls:
        return

    r, c, d = mid_N, mid_N, -1
    ball_no, ball_count = balls.popleft()

    size = 0  # 나선의 한 변 크기
    while True:
        size += 1
        for _ in range(2):
            d = (d + 1) % 4
            for _ in range(size):
                nr, nc = r + drdc[d][0], c + drdc[d][1]
                if not is_valid(nr, nc):
                    return

                r, c = nr, nc
                if not balls and ball_count == 0:
                    board[nr][nc] = 0
                    continue

                if ball_count == 0:
                    ball_no, ball_count = balls.popleft()

                board[nr][nc] = ball_no
                ball_count -= 1


# 구슬 변화 (구슬 그룹 -> 그룹에 들어있는 구슬의 수, 그룹을 이루는 구슬 번호)
def change(balls):
    for _ in range(len(balls)):
        ball_no, ball_count = balls.popleft()
        balls.append([ball_count, 1])
        balls.append([ball_no, 1])


# ←, ↓, →, ↑
drdc = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# ↑, ↓, ←, → (1, 2, 3, 4) -> ←, ↓, →, ↑ 로 변경해주는 맵
d_map = [-1, 3, 1, 0, 2]
# N: 격자 크기, M: 마법 실행 횟수
N, M = map(int, read().split())
# explode_count: 각 구슬(1 ~ 3)의 폭발한 개수
explode_count = [0] * 4
# mid_N: 상어의 위치
mid_N = N // 2
# 격자의 구슬 정보
board = [list(map(int, read().split())) for _ in range(N)]

# 마법 시전
for _ in range(M):
    # d 방향으로 거리가 s 이하인 모든 칸의 구슬 파괴
    d, s = map(int, read().split())
    destroy(d, s)

    balls = get_balls()
    balls = explode(balls)
    change(balls)
    set_balls(balls)


total = 0
for i in range(1, 3 + 1):
    total += i * explode_count[i]
print(total)
