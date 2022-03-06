import sys
read = sys.stdin.readline


# 블록을 추가한다
def add_block(x1, y1, x2, y2, board):
    # 블록을 얹을 행을 찾는다
    top = 0
    for top in range(5 + 1):
        if board[top][y1] == 1 or board[top][y2] == 1:
            top -= 1
            break

    board[top][y1] = 1
    if x1 - x2 == -1:  # 위아래 블록이라면
        board[top - 1][y1] = 1
    elif y1 - y2 == -1:  # 좌우 블록이라면
        board[top][y2] = 1


# 네 칸이 모두 찬 곳이 있다면 그 칸들을 비우고 점수를 얻는다
def get_score(board):
    score = 0

    for top in range(6):  # 위에서부터 확인
        if sum(board[top]) == 4:  # 모든 칸이 1인 행이 있다면
            score += 1
            # 그 행의 윗칸들은 한 칸씩 아래로 이동
            for x in range(top, 0, -1):  # 행별로 반복
                for y in range(4):  # 열별로 반복
                    board[x][y] = board[x - 1][y]

    return score


# 특별 칸에 블록이 생기면 index만큼 바깥쪽으로 밀어낸다
def move(index, board):
    # 바깥쪽으로 index칸만큼 이동
    for x in range(5, index - 1, -1):  # 아래부터 행별로 반복
        for y in range(4):  # 열별로 반복
            board[x][y] = board[x - index][y]
    # 특별 칸들은 0으로 설정
    for x in range(2):  # 행별로 반복
        for y in range(4):  # 열별로 반복
            board[x][y] = 0


blocks = [[], [0, 0], [0, 1], [1, 0]]  # t에 따른 추가 블록(오른쪽 또는 아래)
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]  # blue는 시계 방향으로 90도 회전한 모양(x,y가 바뀜)

N = int(read())  # 블록을 놓을 횟수
score = 0
for _ in range(N):
    # t - 1: 크기 1x1, 2: 크기 1x2(좌우블록), 3: 크기 2x1(상하블록)
    # x: 행, y: 열
    t, x, y = map(int, read().split())
    # nx, ny: t에 따른 추가 블록(1일 때는 x, y 와 같은 값)
    nx, ny = x + blocks[t][0], y + blocks[t][1]

    add_block(x, y, nx, ny, green)  # 초록 보드에 추가
    add_block(y, x, ny, nx, blue)  # 파란 보드에 추가

    score += get_score(green) + get_score(blue)

    index = 0
    if sum(green[0]) > 0:
        index += 1
    if sum(green[1]) > 0:
        index += 1
    if index > 0:
        move(index, green)

    index = 0
    if sum(blue[0]) > 0:
        index += 1
    if sum(blue[1]) > 0:
        index += 1
    if index > 0:
        move(index, blue)


block_count = 0
for x in range(2, 6):
    block_count += sum(green[x]) + sum(blue[x])

print(score)
print(block_count)
