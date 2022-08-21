import sys
read = sys.stdin.readline


# 두 선분이 서로 만나는지 확인 (이동 중 몇초에 만나는지 반환)
# 1: 새로 뱀이 이동중인 경로의 선분
# 2: 이전에 이미 이동한 경로의 선분
def check(r1, c1, d1, len1, r2, c2, d2, len2):
    # 세로: 0, 가로: 1
    row_or_col_1, row_or_col_2 = d1 % 2, d2 % 2

    # 두 선분 모두 세로
    if row_or_col_1 == 0 and row_or_col_2 == 0:
        if c1 == c2 and (r1 <= r2 <= r1 + len1 or r2 <= r1 <= r2 + len2):
            # 새로운 선분이 위에 있을 경우 (아래 방향)
            if r1 <= r2:
                return r2 - r1
            # 새로운 선분이 밑에 있을 경우 (위 방향)
            else:
                return (r1 + len1) - (r2 + len2)
    # 두 선분 모두 가로
    elif row_or_col_1 == 1 and row_or_col_2 == 1:
        if r1 == r2 and (c1 <= c2 <= c1 + len1 or c2 <= c1 <= c2 + len2):
            # 새로운 선분이 왼쪽에 있을 경우 (오른쪽 방향)
            if c1 <= c2:
                return c2 - c1
            # 새로운 선분이 오른쪽에 있을 경우 (왼쪽 방향)
            else:
                return (c1 + len1) - (c2 + len2)
    # 새로운 선분은 세로, 이전 선분은 가로
    elif row_or_col_1 == 0 and row_or_col_2 == 1:
        if r1 <= r2 <= r1 + len1 and c2 <= c1 <= c2 + len2:
            # 새로운 선분 아래 방향
            if d1 == 2:
                return r2 - r1
            # 새로운 선분 위 방향
            else:
                return (r1 + len1) - r2
    # 새로운 선분은 가로, 이전 선분은 세로
    elif row_or_col_1 == 1 and row_or_col_2 == 0:
        if r2 <= r1 <= r2 + len2 and c1 <= c2 <= c1 + len1:
            # 새로운 선분 오른쪽 방향
            if d1 == 1:
                return c2 - c1
            # 새로운 선분 왼쪽 방향
            else:
                return (c1 + len1) - c2

    return -1


# 이번 선분에 대해 만나는 선분이 있는지 확인
# r, c: 시작 위치
# r1, c1: 선분의 두 끝 중 왼쪽 위의 점
def check_all(r, c, r1, c1, d1, len1):
    # 첫 번째 이동인 경우
    if not snake:
        return -1

    result = float('inf')

    # 직전 선분을 제외한 모든 선분 확인
    for i in range(len(snake) - 1):
        r2, c2, d2, len2 = snake[i]
        now_result = check(r1, c1, d1, len1, r2, c2, d2, len2)
        # 만나는 선분이 있다면
        if now_result > -1:
            result = min(result, now_result)
    # 이번 선분의 직전 선분은 마지막 위치가 겹치기 때문에 따로 처리
    new_r1 = min(r + drdc[d1][0], r + (drdc[d1][0] * len1))
    new_c1 = min(c + drdc[d1][1], c + (drdc[d1][1] * len1))
    now_result = check(new_r1, new_c1, d1, len1 - 1, *snake[-1])
    if now_result > -1:
        result = min(result, now_result)

    return -1 if result == float('inf') else result


drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
rotate_map = {'R': 1, 'L': 3}

SIZE = 2 * int(read()) + 1  # 격자의 실제 크기
N = int(read())  # 방향 회전 수

move_info = [list(read().strip().split()) for _ in range(N)]  # 입력받은 뱀 방향전환 정보
move_info.append([str(SIZE), 'L'])  # 중간에 죽지 않을 경우 대비

snake = []  # 뱀 정보(선분) [[왼쪽 위 행, 왼쪽 위 열, 방향, 길이], ...]
time_sum, end_time = 0, -1  # 시각, 뱀이 죽은 시각
r, c, d = SIZE // 2, SIZE // 2, 1  # 머리의 행, 열 위치(선분의 한쪽 끝), 방향
for time_str, rotate_str in move_info:
    time = int(time_str)

    if time == 0:
        continue

    # 선분의 다른 한쪽 끝
    nr, nc = r + (drdc[d][0] * time), c + (drdc[d][1] * time)

    # move_info 마지막에 최대 길이의 선분을 넣었기 때문에 범위보다 겹치는지 먼저 확인!!
    # 1. 다른 선분과 겹치는지 확인
    check_result = check_all(r, c, min(r, nr), min(c, nc), d, time)
    # 겹치는 선분 존재
    if check_result > -1:
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

    # 이번에 생성한 선분 저장
    snake.append((min(r, nr), min(c, nc), d, time))

    # 방향 전환
    d = (d + rotate_map[rotate_str]) % 4

    time_sum += time
    r, c = nr, nc

print(end_time)
