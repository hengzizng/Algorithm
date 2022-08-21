import sys
read = sys.stdin.readline


drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
SIZE = 2 * int(read()) + 1  # 격자의 실제 크기
N = int(read())  # 방향 회전 수
move_info = []  # [(회전 시각, 회전 방향), ...]
time_sum = 1  # 회전해야할 실제 시각(time_sum 시각에 회전하고, 그 방향으로 이동)
for _ in range(N):
    time, d = read().strip().split()
    time_sum += int(time)
    move_info.append((time_sum, 3 if d == 'L' else 1))

board = [[0] * SIZE for _ in range(SIZE)]  # 격자판 상태 (0: 빈 칸, 1: 뱀)
r, c, d = SIZE // 2, SIZE // 2 - 1, 1  # 뱀의 머리 정보 [행, 열, 방향]
move_index = 0  # move_info를 위한 인덱스

for time in range(SIZE * SIZE + 2):  # 현재 시각
    # 회전해야 할 시각이라면
    if time == move_info[move_index][0]:
        d = (d + move_info[move_index][1]) % 4
        move_index += 1

    nr, nc = r + drdc[d][0], c + drdc[d][1]
    if nr < 0 or nr >= SIZE or nc < 0 or nc >= SIZE or board[nr][nc] == 1:
        print(time)
        break

    # 뱀의 머리 이동
    r, c = nr, nc
    board[r][c] = 1
