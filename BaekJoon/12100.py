from collections import deque
import sys
read = sys.stdin.readline


# count: 지금까지 움직인 횟수
def move(count, board):
    if count == 5:
        for r in range(N):
            max_block[0] = max(max_block[0], max(board[r]))
        return

    move(count + 1, up(board))
    move(count + 1, down(board))
    move(count + 1, left(board))
    move(count + 1, right(board))


def up(board):
    new_board = [[0] * N for _ in range(N)]

    for c in range(N):
        queue = deque()

        for r in range(N):
            if board[r][c] > 0:
                queue.append(board[r][c])

        r = 0
        while queue:
            num = queue.popleft()
            if queue and queue[0] == num:
                num += queue.popleft()
            new_board[r][c] = num
            r += 1

    return new_board


def down(board):
    new_board = [[0] * N for _ in range(N)]

    for c in range(N):
        queue = deque()

        for r in range(N - 1, 0 - 1, -1):
            if board[r][c] > 0:
                queue.append(board[r][c])

        r = N - 1
        while queue:
            num = queue.popleft()
            if queue and queue[0] == num:
                num += queue.popleft()
            new_board[r][c] = num
            r -= 1

    return new_board


def left(board):
    new_board = [[0] * N for _ in range(N)]

    for r in range(N):
        queue = deque()

        for c in range(N):
            if board[r][c] > 0:
                queue.append(board[r][c])

        c = 0
        while queue:
            num = queue.popleft()
            if queue and queue[0] == num:
                num += queue.popleft()
            new_board[r][c] = num
            c += 1

    return new_board


def right(board):
    new_board = [[0] * N for _ in range(N)]

    for r in range(N):
        queue = deque()

        for c in range(N - 1, 0 - 1, -1):
            if board[r][c] > 0:
                queue.append(board[r][c])

        c = N - 1
        while queue:
            num = queue.popleft()
            if queue and queue[0] == num:
                num += queue.popleft()
            new_board[r][c] = num
            c -= 1

    return new_board


N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]

max_block = [0]
move(0, board)

print(*max_block)
