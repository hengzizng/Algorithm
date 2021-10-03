import sys

####### 테스트용
sys.stdin = open("TestCase/BaekJoon/19236input.txt")
####### 테스트용

read = sys.stdin.readline


def fish_move(shark, fishes, board):
    for fish in range(1, 16 + 1):
        if fish not in fishes:
            continue
        x, y = fishes[fish]
        d = board[x][y][1]

        # 갈 수 있는 방향을 찾는다.
        can_go = False
        for _ in range(8):
            nx, ny = x + dxdy[d][0], y + dxdy[d][1]
            if range_check(nx, ny) and (nx != shark[0] or ny != shark[1]):
                can_go = True
                break
            d = (d + 1) % 8
        
        if not can_go: # 이동할 수 없으면 가만히 있는다
            continue

        moved_fish = board[nx][ny][0] # 교환할 칸
        
        if moved_fish > 0: # 빈칸이 아닌 다른 물고기와의 위치 교환이면 그 물고기의 위치도 수정해준다
            fishes[moved_fish] = [x, y]

        fishes[fish] = [nx, ny]
        board[x][y], board[nx][ny] = board[nx][ny], (fish, d)

        # print()
        # print("물고기:", fish, moved_fish, "방향:", d, "위치:", x, y, "->", nx, ny)
        # print_board(board)

def eat(eat_sum, shark, fishes, board):
    x, y, d = shark

    new_fishes = {}
    for fish, loc in fishes.items():
        new_fishes[fish] = loc
    
    new_board = []
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[i][j])

    # print("-----------------------------------")
    # print("먹기 전 >", shark, eat_sum)
    # print_board(new_board)

    del new_fishes[new_board[x][y][0]]
    eat_sum += new_board[x][y][0]
    new_board[x][y] = (0, 0)

    # print("먹은 뒤 >", shark, eat_sum)
    # print_board(new_board)

    fish_move(shark, new_fishes, new_board)

    # print("물고기 움직인 뒤 >", shark, eat_sum)
    # print_board(new_board)

    can_go = False
    nx, ny = x + dxdy[d][0], y + dxdy[d][1]
    while range_check(nx, ny):
        new_shark = [nx, ny, new_board[nx][ny][1]]
        if new_board[nx][ny] != (0, 0):
            eat(eat_sum, new_shark, new_fishes, new_board)
            can_go = True # 상어가 갈 수 있는 곳이 한군데라도 있다면 True
        nx += dxdy[d][0]
        ny += dxdy[d][1]
    
    if not can_go:
        eat_max_sum[0] = max(eat_max_sum[0], eat_sum)



def range_check(x, y):
    if 0 <= x < 4 and 0 <= y < 4:
        return True
    return False

def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()

dxdy = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
board = [] # board의 각 칸 : (물고기 번호, 방향)
fishes = {} # 물고기들의 위치 저장 [x, y]
for i in range(4):
    board.append([])
    temp = list(map(int, read().split()))
    for j in range(0, 8, 2):
        board[i].append((temp[j], temp[j + 1] - 1))
        fishes[temp[j]] = [i, j // 2]

shark = [0, 0, board[0][0][1]] # x좌표, y좌표, 방향
eat_max_sum = [0] # 상어가 먹은 물고기 번호의 합의 최댓값

# print_board(board)
eat(0, shark, fishes, board)

# print_board(board)
# del fishes[16]
# board[0][0] = (0, 0)
# fish_move(shark, fishes, board)
# print()
# print_board(board)

print(eat_max_sum[0])