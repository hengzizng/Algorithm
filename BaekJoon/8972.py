from collections import defaultdict
import sys
sys.stdin = open("TestCase/BaekJoon/8972input.txt")
read = sys.stdin.readline


# 보드의 상태를 출력
def print_board():
    for r in range(R):
        print(''.join(board[r]))


# 미친 아두이노들이 이동 (중간에 게임이 끝났다면 False 반환)
def move_arduinos():
    # 3. 미친 아두이노들이 종수의 아두이노와 가장 가까워지는 방향으로 한 칸 이동
    # 위치별 아두이노 번호 리스트
    arduinos_locs = defaultdict(list)
    for no in range(len(arduinos)):
        # 파괴된 아두이노라면 이동하지 X
        if is_destroied[no]:
            continue

        # 이동할 방향을 찾는다.
        if jongsu[0] == arduinos[no][0]:
            dr = 0
        elif jongsu[0] < arduinos[no][0]:
            dr = -1
        else:
            dr = 1
        if jongsu[1] == arduinos[no][1]:
            dc = 0
        elif jongsu[1] < arduinos[no][1]:
            dc = -1
        else:
            dc = 1

        # 이동 (board에 표시는 아래에서 한번에 해준다.)
        board[arduinos[no][0]][arduinos[no][1]] = '.'
        arduinos[no][0] += dr
        arduinos[no][1] += dc
        arduinos_locs[(arduinos[no][0], arduinos[no][1])].append(no)

        # 4. 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동했다면 종료
        if arduinos[no][0] == jongsu[0] and arduinos[no][1] == jongsu[1]:
            return False

    # 5. 2개 또는 그 이상의 미친 아두이노가 같은 칸에 있는 경우
    for loc in arduinos_locs.keys():
        if len(arduinos_locs[loc]) >= 2:
            for no in arduinos_locs[loc]:
                is_destroied[no] = True
        else:
            board[loc[0]][loc[1]] = 'R'

    return True


# 방향 벡터
drdc = [[1, -1], [1, 0], [1, 1],
        [0, -1], [0, 0], [0, 1],
        [-1, -1], [-1, 0], [-1, 1]]
# 보드의 행 수, 열 수
R, C = map(int, read().split())
# 보드 상태
board = [list(read().strip()) for _ in range(R)]
# 종수가 움직이려는 방향 리스트
commands = list(map(lambda x: int(x) - 1, list(read().strip())))

# 종수의 아두이노 위치
jongsu = []
# 미친 아두이노들의 위치
arduinos = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'I':
            board[r][c] = '.'
            jongsu = [r, c]
        elif board[r][c] == 'R':
            arduinos.append([r, c])
# 미친 아두이노들이 파괴되었는지 여부
is_destroied = [False] * len(arduinos)

# 종수가 움직인 횟수
move_count = 0
# 종수가 이겼는지 여부
is_win = True
for command in commands:
    # 1. 종수 이동
    jongsu[0] += drdc[command][0]
    jongsu[1] += drdc[command][1]
    move_count += 1
    # 2. 미친 아두이노가 있는 칸이면 종료
    # move_arduinos: 3, 4, 5 과정
    if board[jongsu[0]][jongsu[1]] == 'R' or not move_arduinos():
        is_win = False
        break

if is_win:
    board[jongsu[0]][jongsu[1]] = 'I'
    print_board()
else:
    print("kraj", move_count)
