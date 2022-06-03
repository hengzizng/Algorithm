import sys
# 테스트용
sys.stdin = open("TestCase/BaekJoon/19237input.txt")
# 테스트용
read = sys.stdin.readline


def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
    print()


def check_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def move(time):
    new_board = [[(0, 0)] * N for _ in range(N)]  # (냄새를 남긴 상어 번호, 냄새를 남긴 시각)

    for x in range(N):
        for y in range(N):
            # 상어가 없고 냄새만 남은 곳이면 new_board에 옮겨준다.
            if time - k < board[x][y][1] <= time - 1:
                new_board[x][y] = board[x][y]

    del_sharks = set()
    for shark, shark_loc in sharks_loc.items():  # shark: 이번에 이동할 상어 번호
        x, y = shark_loc  # 현재 위치
        now_d = sharks_d[shark]  # 현재 방향

        is_find = False  # 이동할 칸을 찾았는지 여부
        priority = sharks_info[shark][now_d]  # 현재 방향의 우선순위

        for i in priority:  # 우선순위에 따라 이동할 칸의 상태 확인
            nx, ny = dxdy[i][0] + x, dxdy[i][1] + y
            # 빈 칸이라면
            if check_range(nx, ny) and (board[nx][ny][0] == 0 or (time - board[nx][ny][1]) > k):
                # print("> 상어:", shark, "방향:", now_d, "바뀔방향:", i, "위치:", x, y, "->", nx, ny)
                sharks_d[shark] = i  # 상어의 방향을 바꿔준다.
                is_find = True
                break

        if not is_find:  # 주변에 빈 칸이 없다면
            for i in priority:  # 우선순위에 따라 이동할 칸의 상태 확인
                nx, ny = dxdy[i][0] + x, dxdy[i][1] + y
                # 자신의 냄새가 있는 칸이라면
                if check_range(nx, ny) and board[nx][ny][0] == shark:
                    # print(">> 상어:", shark, "방향:", now_d, "바뀔방향:", i, "위치:", x, y, "->", nx, ny)
                    sharks_d[shark] = i  # 상어의 방향을 바꿔준다.
                    break

        # print(">>> 상어:", shark, "위치:", x, y, "->", nx, ny)
        if 0 < new_board[nx][ny][0] < shark:  # 이동할 칸에 번호가 더 작은 상어가 있다면
            shark_count[0] -= 1
            del_sharks.add(shark)
            continue
        if 0 < shark < new_board[nx][ny][0]:  # 이동할 칸에 번호가 더 큰 상어가 있다면
            shark_count[0] -= 1
            del_sharks.add(new_board[nx][ny][0])
        sharks_loc[shark] = (nx, ny)
        new_board[nx][ny] = (shark, time)

    for del_shark in del_sharks:
        del sharks_loc[del_shark]

    return new_board


dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 위(0), 아래(1), 왼쪽(2), 오른쪽(3)
N, M, k = map(int, read().split())  # N: 격자의 크기, M: 상어의 수, k: 상어의 냄새 유지 시간

shark_count = [M]  # 격자판에 남은 상어의 수

board = []  # 상어들이 들어있는 격자
sharks_loc = {}  # 상어들의 위치
for i in range(N):
    board.append(list(map(int, read().split())))
    for j in range(N):  # 초기 상태
        shark = board[i][j]
        board[i][j] = (shark, 0)  # (냄새를 남긴 상어 번호, 냄새를 남긴 시각)
        if shark > 0:
            sharks_loc[shark] = (i, j)

sharks_d = {}  # 각 상어의 방향
temp = list(map(int, read().split()))
for i, d in enumerate(temp, 1):  # 상어 번호는 1부터 시작
    sharks_d[i] = d - 1  # 방향은 0부터 시작

sharks_info = {}  # 각 상어의 방향 우선순위
for shark in range(1, M + 1):
    sharks_info[shark] = []
    for _ in range(4):
        temp = list(map(lambda x: int(x) - 1, read().split()))
        sharks_info[shark].append(temp)

answer = -1
for time in range(1, 1000 + 1):
    board = move(time)

    # print("time:", time, "count:", shark_count[0])
    # print(sharks_d)
    # print_board(board)

    if shark_count[0] == 1:
        answer = time
        break
print(answer)
