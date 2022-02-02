# 지도의 크기: N dice_loc[0] M

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
# 지도의 바깥으로 이동하는 명령은 무시

# 칸: 0 <- 주사위 바닥 수
# 칸: 수 -> 주사위 바닥 (칸 0으로 변경)

#           2(뒷면)
# 4(서쪽면) 1(윗면) 3(동쪽면)
#           5(앞면)
#           6(아랫면)
# 일 때 dice = [1, 5, 6, 2, 4, 3]

import sys
read = sys.stdin.readline


def go_south():  # 남쪽으로
    temp = dice[3]
    for i in range(3, 1 - 1, -1):
        dice[i] = dice[i - 1]
    dice[0] = temp


def go_north():  # 북쪽으로
    temp = dice[0]
    for i in range(0, 2 + 1):
        dice[i] = dice[i + 1]
    dice[3] = temp


def go_east():  # 동쪽으로
    temp = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[0]
    dice[0] = dice[4]
    dice[4] = temp


def go_west():  # 서쪽으로
    temp = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[5]
    dice[5] = dice[2]
    dice[2] = temp


def copy_number():  # 칸 <-> 주사위 바닥 으로 복사
    if board[dice_loc[0]][dice_loc[1]] == 0:
        board[dice_loc[0]][dice_loc[1]] = dice[2]
    else:
        dice[2] = board[dice_loc[0]][dice_loc[1]]
        board[dice_loc[0]][dice_loc[1]] = 0


def execute_command(command):
    is_excuted = False

    if command == 1:  # 동쪽
        if dice_loc[1] + 1 < M:
            dice_loc[1] += 1
            go_east()
            is_excuted = True
    elif command == 2:  # 서쪽
        if dice_loc[1] - 1 >= 0:
            dice_loc[1] -= 1
            go_west()
            is_excuted = True
    elif command == 3:  # 북쪽
        if dice_loc[0] - 1 >= 0:
            dice_loc[0] -= 1
            go_north()
            is_excuted = True
    elif command == 4:  # 남쪽
        if dice_loc[0] + 1 < N:
            dice_loc[0] += 1
            go_south()
            is_excuted = True

    if is_excuted:
        copy_number()

    return is_excuted


dice = [0] * 6

N, M, x, y, K = map(int, read().split())
dice_loc = [x, y]

board = []
for _ in range(N):
    board.append(list(map(int, read().split())))

commands = list(map(int, read().split()))
for command in commands:
    if execute_command(command):
        print(dice[0])
