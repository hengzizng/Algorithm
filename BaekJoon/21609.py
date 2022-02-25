# 무려 3시간 반...

# 블록 색상 => -1: 검은색, 0: 무지개, 1 ~ M: 일반 블록 색상

# 블록 그룹
# - 같은 색의 일반 블록 1개 이상
# - 검은색 블록 미포함
# - 무지개 블록 상관 X
# - 블록의 개수는 2개 이상

# 기준 블록 : 일반 블록 중 블록 그룹 중 가장 위쪽 왼쪽

# ----- 블록 그룹이 존재하는동안 반복 ------
# 1. 크기가 가장 큰 블록 그룹을 찾는다
#    크기가 같으면, 무지개 블록의 수가 가장 많은 그룹
#    무지개 블록 수도 같으면, 기준 블록이 가장 !!!!!아래쪽 오른쪽!!!!!
# 2. 찾은 블록 그룹의 모든 블록 제거 -> (블록 수)^2 점 획득
# 3. 검은색 블록을 제외한 모든 블록 가장 아래로 이동
# 4. 보드 반시계 방향으로 90도 회전
# 5. 검은색 블록을 제외한 모든 블록 가장 아래로 이동
# ------------

from collections import deque
import sys
read = sys.stdin.readline


# 블록 그룹을 찾고 그 크기를 반환한다.
def get_group(r, c, board, checked):
    color, rainbow_count = board[r][c], 0  # 일반 블록 색상, 무지개블록 수
    queue, group = deque(), set()

    queue.append((r, c))
    group.add((r, c))
    checked[r][c] = True

    while queue:
        r, c = queue.popleft()

        if board[r][c] == 0:
            rainbow_count += 1

        # 인접한 블록들을 확인
        for dr, dc in drdc:
            dr, dc = dr + r, dc + c
            if (
                dr < 0 or dr >= N or dc < 0 or dc >= N or
                (dr, dc) in group or checked[dr][dc] or board[dr][dc] <= -1
            ):
                continue

            if board[dr][dc] == color:  # 전역 방문체크에는 일반 블록일 때만 방문체크
                checked[dr][dc] = True

            if board[dr][dc] == color or board[dr][dc] == 0:
                group.add((dr, dc))
                queue.append((dr, dc))

    return rainbow_count, group


# 검은색 블록을 제외한 모든 블록 아래로 이동
def down(board):
    for c in range(N):
        for r in range(N - 1, 0 - 1, -1):
            if board[r][c] < 0:
                continue

            new_r, target = r + 1, board[r][c]
            while new_r < N and board[new_r][c] == -2:
                new_r += 1

            board[r][c] = -2
            board[new_r - 1][c] = target


# 반시계 방향으로 90도 회전
def rotate(board):
    new_board = []

    for r in range(N):
        new_board.append([])
        for c in range(N):
            new_board[r].append(board[c][N - 1 - r])

    return new_board


# 크기가 가장 큰 그룹을 찾아 삭제 후 그 크기를 반환
def delete_group(board):
    checked = [[False] * N for _ in range(N)]

    max_group = set()  # 크기가 가장 큰 그룹
    max_group_info = [-1, N, -1]  # 크기가 가장 큰 그룹의 기준 블록 행, 열, 무지개블록 수
    for r in range(N):
        for c in range(N):
            if not checked[r][c] and board[r][c] >= 1:
                # 그룹을 찾는다
                rainbow_count, group = get_group(r, c, board, checked)

                # 이미 찾아둔 그룹보다 크기가 작다면
                if len(group) < len(max_group):
                    continue

                # 이미 찾아둔 그룹보다 크기가 더 크다면
                if len(group) > len(max_group):
                    max_group_info = [r, c, rainbow_count]
                    max_group = group
                    continue

                # 이미 찾아둔 그룹과 크기가 같은데 무지개블록 수가 더 작다면
                if rainbow_count < max_group_info[2]:
                    continue

                # 이미 찾아둔 그룹과 크기가 같은데 무지개블록 수가 더 크다면
                if rainbow_count > max_group_info[2]:
                    max_group_info = [r, c, rainbow_count]
                    max_group = group
                    continue

                # 이미 찾아둔 그룹과 크기가 같은데 무지개블록 수도 같다면 기준 블록이 가장 아래, 오른쪽
                if r > max_group_info[0] or (r == max_group_info[0] and c > max_group_info[1]):
                    max_group_info = [r, c, rainbow_count]
                    max_group = group

    for r, c in max_group:
        board[r][c] = -2

    return len(max_group)


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, read().split())  # N: 보드의 크기, M: 일반 블록의 색상 수
board = [list(map(int, read().split())) for _ in range(N)]
score = 0

while True:
    size = delete_group(board)
    if size <= 1:
        break
    score += size ** 2

    down(board)
    board = rotate(board)
    down(board)

print(score)
