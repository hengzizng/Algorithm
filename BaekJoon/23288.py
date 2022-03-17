# 75 min

from collections import deque
import sys
read = sys.stdin.readline


# (r, c) 값이 지도 내에 유효한지 판단하는 함수
def is_valid(r, c):
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    else:
        return True


# 주사위가 이동 방향으로 한 칸 굴러가는 함수
def move(dice, dice_val):
    nr = dice[0] + dr[dice[2]]
    nc = dice[1] + dc[dice[2]]

    # 이동 방향에 칸이 없다면 이동 방향 반대로 변경
    if not is_valid(nr, nc):
        dice[2] = (dice[2] + 2) % 4
        nr = dice[0] + dr[dice[2]]
        nc = dice[1] + dc[dice[2]]

    # 주사위 각 면들의 값 변경
    temp = dice_val[0]
    for i in range(3):
        d = direction_order[dice[2]][i]
        nd = direction_order[dice[2]][i + 1]
        dice_val[d] = dice_val[nd]
    dice_val[nd] = temp

    # 주사위의 위치 변경
    dice[0] = nr
    dice[1] = nc


# 주사위가 위치한 칸(r, c)의 점수를 구하는 함수
def get_score(r, c, board, scores):
    # 이미 점수를 구해놓은 칸이라면 바로 return
    if scores[r][c] > 0:
        return scores[r][c]

    # bfs로 주사위가 위치한 칸의 숫자(B)와 같은 숫자인 칸들을 구한다.
    target_score = board[r][c]
    queue = deque([(r, c)])
    checked = set([(r, c)])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_valid(nr, nc) and board[nr][nc] == target_score and (nr, nc) not in checked:
                checked.add((nr, nc))
                queue.append((nr, nc))

    # 점수를 계산(B * 칸 개수)해 위에서 구한 칸들에 모두 표기해준다.
    now_score = target_score * len(checked)
    for r, c in checked:
        scores[r][c] = now_score

    return now_score


# 주사위의 이동 방향을 결정하는 함수
def set_direction(board_num, dice, dice_val):
    # 주사위 아랫면 수 > 칸 숫자 : 이동 방향 90도 시계 방향으로 회전
    if dice_val[2] > board_num:
        dice[2] = (dice[2] + 1) % 4
    # 주사위 아랫면 수 < 칸 숫자 : 이동 방향 90도 반시계 방향으로 회전
    elif dice_val[2] < board_num:
        dice[2] = (dice[2] + 3) % 4
    # 주사위 아랫면 수 = 칸 숫자 : 이동 방향 변화 X


# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 북, 동, 남, 서 별로 주사위가 이동하면 값을 변경해주기 위한 순서
direction_order = [
    [0, 1, 2, 3],
    [0, 4, 2, 5],
    [0, 3, 2, 1],
    [0, 5, 2, 4]
]
# 행 수, 열 수, 이동 횟수
N, M, K = map(int, read().split())
# 지도 정보 (10 미만의 자연수)
board = [list(map(int, read().split())) for _ in range(N)]
# 각 위치별 점수, 아직 점수가 구해지지 않은 칸은 0
scores = [[0] * M for _ in range(N)]
# 행 위치, 열 위치, 방향
dice = [0, 0, 1]
# [윗면, 앞면, 아랫면, 뒷면, 왼쪽면, 오른쪽면] 의 숫자
dice_val = [1, 5, 6, 2, 4, 3]
# 각 이동에서 획득하는 점수의 합
total_score = 0

for k in range(K):
    move(dice, dice_val)  # 주사위 이동
    total_score += get_score(dice[0], dice[1], board, scores)  # 점수 획득
    set_direction(board[dice[0]][dice[1]], dice, dice_val)  # 이동 방향 결정

print(total_score)
