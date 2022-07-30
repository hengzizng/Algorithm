import sys
read = sys.stdin.readline


# robot이 움직인 뒤 결과를 반환한다.
# 문제 없는 경우 0, 벽에 충돌한 경우 -1, 다른 로봇과 충돌한 경우 그 로봇 번호
def move(robot, command, repeat):
    # 방향만 바꾸는 경우
    if command != 0:
        repeat = repeat % 4
        # 명령에 따라 바뀐 방향
        robots[robot][2] = (robots[robot][2] + (command * repeat)) % 4
        return 0

    r, c, d = robots[robot]
    nr, nc = r, c
    for _ in range(repeat):
        # 명령에 따라 이동한 위치
        nr, nc = drdc[d][0] + nr, drdc[d][1] + nc
        if nr < 0 or nr >= B or nc < 0 or nc >= A:
            return -1
        if land[nr][nc] > 0:
            return land[nr][nc]

    land[nr][nc] = land[r][c]
    land[r][c] = 0
    robots[robot][0], robots[robot][1] = nr, nc
    return 0


# 방향 벡터 (상우하좌)
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 방향 문자 -> 숫자 변환 맵
dir_map = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
# 명령 -> 방향 변화값 변환 맵
command_map = {'L': 3, 'R': 1, 'F': 0}
# A: 가로 크기(열 수), B: 세로 크기(행 수)
A, B = map(int, read().split())
# N: 로봇 수, M: 명령 수
N, M = map(int, read().split())

# 로봇 정보 저장
# 로봇별 위치와 방향
robots = [[-1, -1, -1]]
# 땅의 현재 상태 (0: 비어있는 땅, 1이상: 로봇)
land = [[0] * A for _ in range(B)]
for robot in range(1, N + 1):
    # x: 가로 위치, y: 세로 위치, d: 방향
    x, y, d = read().strip().split()
    # r: 행, c: 열
    r, c, d = B - int(y), int(x) - 1, dir_map[d]
    land[r][c] = robot
    robots.append([r, c, d])

is_crash = False
for _ in range(M):
    a, b, c = read().strip().split()
    # robot: 로봇 번호, command: 명령, repeat: 명령 반복 횟수
    robot, command, repeat = int(a), command_map[b], int(c)

    if is_crash:
        continue

    result = move(robot, command, repeat)
    if result == 0:
        continue

    is_crash = True
    if result == -1:
        print("Robot %d crashes into the wall" % robot)
    else:
        print("Robot %d crashes into robot %d" % (robot, result))

if not is_crash:
    print("OK")
