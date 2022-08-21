import sys
read = sys.stdin.readline


# 확인하려는 선분이 세로일 경우 겹치는 선분이 있는지 체크 (없을 경우 0 반환)
def col_check(r, c, d, length):
    # 확인하려는 선분의 위쪽
    up_r = min(r, r + (drdc[d][0] * length))

    # 이전의 모든 선분과 겹치는지 확인
    for nr, nc, nd, nlength in snake:
        # 이번 선분도 세로일 경우
        if nd == 0:
            if c != nc or nr + nlength <= up_r or up_r + length <= nr:
                continue
            # 이번 선분과 겹칠 경우 (겹치는데 몇 초 걸리는지 반환)
            # 뱀의 진행 방향에 따라 계산
            return (r - (nr + length)) if d == 0 else (nr - r)
        # 이번 선분은 가로일 경우
        else:
            # 이번 선분과 겹칠 경우 (겹치는데 몇 초 걸리는지 반환)
            if up_r < nr < up_r + length and nc < c < nc + nlength:
                return abs(r - nr)

    return 0


# 확인하려는 선분이 가로일 경우 겹치는 선분이 있는지 체크 (없을 경우 0 반환)
def row_check(r, c, d, length):
    # 확인하려는 선분의 왼쪽, 오른쪽
    left_c = min(c, c + (drdc[d][1] * length))

    # 이전의 모든 선분과 겹치는지 확인
    for nr, nc, nd, nlength in snake:
        # 이번 선분은 세로일 경우
        if nd == 0:
            # 이번 선분과 겹칠 경우 (겹치는데 몇 초 걸리는지 반환)
            if nr < r < nr + nlength and left_c < nc < left_c + length:
                return abs(c - nc)

        # 이번 선분도 가로일 경우
        else:
            if r != nr or nc + nlength <= left_c or left_c + length <= nc:
                continue
            # 이번 선분과 겹칠 경우 (겹치는데 몇 초 걸리는지 반환)
            return (nc - c) if d == 1 else (c - (nc + nlength))

    return 0


drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
L = int(read())
SIZE = 2 * L + 1  # 격자의 실제 크기
N = int(read())  # 방향 회전 수
move_info = [list(read().strip().split()) for _ in range(N)]  # 뱀 방향전환 정보
move_info.append([str(SIZE), 'L'])  # 중간에 죽지 않을 경우 대비

snake = []  # 뱀 정보(선분) [[왼쪽 위 행, 왼쪽 위 열, 방향(0: 세로, 1: 가로), 길이], ...]

time_sum, end_time = 0, -1  # 시각, 뱀이 죽은 시각
r, c, d = SIZE // 2, SIZE // 2, 1  # 머리의 행, 열 위치, 방향
for time_str, d_str in move_info:
    time = int(time_str)

    # 선분의 다른 한쪽 끝
    nr, nc = r + (drdc[d][0] * time), c + (drdc[d][1] * time)

    # move_info 마지막에 최대 길이의 선분을 넣었기 때문에 범위보다 겹치는지 먼저 확인!!
    # 1. 다른 선분과 겹치는지 확인
    check_result = col_check(r, c, d, time) if c == nc else row_check(r, c, d, time)
    # 겹친다면 종료
    if check_result > 0:
        end_time = time_sum + check_result
        break

    # 2. 선분이 범위를 벗어난다면 종료
    # 위쪽 범위를 벗어났다면
    if nr < 0:
        end_time = time_sum + time + nr + 1
        break
    # 왼쪽 범위를 벗어났다면
    elif nc < 0:
        end_time = time_sum + time + nc + 1
        break
    # 아래쪽 범위를 벗어났다면
    elif nr >= SIZE:
        end_time = time_sum + time - (nr - SIZE)
        break
    # 오른쪽 범위를 벗어났다면
    elif nc >= SIZE:
        end_time = time_sum + time - (nc - SIZE)
        break

    # 선분 생성
    snake.append((min(r, nr), min(c, nc), 0 if c == nc else 1, time))

    # 방향 전환
    d = (d + (3 if d_str == 'L' else 1)) % 4

    time_sum += time
    r, c = nr, nc

print(end_time)
