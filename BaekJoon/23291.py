import sys
read = sys.stdin.readline


# 물고기의 수가 가장 적은 어항들에 물고기 한마리 추가
def add_fish():
    for c in range(N):
        if board[N - 1][c] == fish_count[0]:
            board[N - 1][c] += 1


# 2층 이상의 어항들 전체 90도 회전해서 바닥의 어항 위에
def build1():
    # 몇 번째 열부터 몇 번째 열까지가 2층 이상인지 찾는다.
    left, right = N, 0
    for c in range(N):
        if board[N - 2][c] > 0:
            left = min(left, c)
            right = max(right, c)

    # 2층 이상인 열들의 가장 위에 있는 어항의 인덱스를 찾는다.
    top = 0
    for r in range(N):
        if board[r][left] > 0:
            top = r
            break

    # 회전시켜서 위에 올려놓을 어항의 높이가 놓을 수 있는 자리의 길이보다 길다면 불가능
    if N - 1 - right < N - top:
        return False

    for c in range(right, left - 1, -1):
        for r in range(N - 1, top - 1, -1):
            # print(r, c, "->", N - 2 - (right - c), right + (N - 1 - r))
            board[N - 2 - (right - c)][right + 1 + (N - 1 - r)] = board[r][c]
            board[r][c] = 0
    
    return True


# 물고기의 수 조절 (인접한 두 어항에 대해 (5 // diff) 만큼 조절)
def adjust():
    adjust_values = []

    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue

            # 현재 칸과 오른쪽 칸
            if c + 1 < N and board[r][c + 1] > 0:
                adjust_value = abs(board[r][c] - board[r][c + 1]) // 5
                
                if adjust_value > 0:
                    if board[r][c] < board[r][c + 1]:
                        adjust_values.append((r, c, adjust_value))
                        adjust_values.append((r, c + 1, -1 * adjust_value))
                    else:
                        adjust_values.append((r, c, -1 * adjust_value))
                        adjust_values.append((r, c + 1, adjust_value))

            # 현재 칸과 아래 칸
            if r + 1 < N and board[r + 1][c] > 0:
                adjust_value = abs(board[r][c] - board[r + 1][c]) // 5

                if adjust_value > 0:
                    if board[r][c] < board[r + 1][c]:
                        adjust_values.append((r, c, adjust_value))
                        adjust_values.append((r + 1, c, -1 * adjust_value))
                    else:
                        adjust_values.append((r, c, -1 * adjust_value))
                        adjust_values.append((r + 1, c, adjust_value))
    
    for r, c, value in adjust_values:
        board[r][c] += value


# 어항들을 바닥에 일렬로 정렬 (왼쪽 아래 -> 왼쪽 위 -> 오른쪽 아래 -> 오른쪽 위)
def sort_in_line():
    bottom = []

    for c in range(N):
        for r in range(N - 1, 0 - 1, -1):
            if board[r][c] == 0:
                continue
            bottom.append(board[r][c])
            board[r][c] = 0

    board[N - 1] = bottom

# 왼쪽 N/2개 180도 회전해서 오른쪽 N/2개 위에 => 2번 반복한 결과
def build2():
    index, c, flag = 0, N - 1, -1
    for r in range(N - 2, N - 5, -1):
        for _ in range(N // 4):
            board[r][c] = board[N - 1][index]
            board[N - 1][index] = 0
            c += flag
            index += 1
        flag *= -1
        c += flag


# -------------- 반복
# add_fish
# 가장 왼쪽의 어항을 그 오른쪽 위로 옮긴다
# build1 => 불가능할 때까지 반복
# adjust
# sort_in_line
# build2
# adjust
# sort_in_line
# 물고기 수의 최댓값, 최솟값 갱신
# 물고기 수의 최댓값 - 최솟값 <= K 이면 종료
# --------------

# N: 어항 수, K: 종료 조건
N, K = map(int, read().split())
# board: 어항들
board = [[0] * N for _ in range(N - 1)]
board.append(list(map(int, read().split())))
# fish_count: 물고기 수의 [최솟값, 최댓값]
fish_count = [min(board[N - 1]), max(board[N - 1])]

count = 0
while True:
    count += 1

    add_fish()

    board[N - 2][1] = board[N - 1][0]
    board[N - 1][0] = 0

    while True:
        if not build1():
            break
    
    adjust()

    sort_in_line()

    build2()

    adjust()

    sort_in_line()

    fish_count[0] = min(board[N - 1])
    fish_count[1] = max(board[N - 1])
    if fish_count[1] - fish_count[0] <= K:
        break

print(count)
