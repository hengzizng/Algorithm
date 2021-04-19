import sys
from collections import deque

read = sys.stdin.readline


def bfs(start_positions):
    queue = deque(start_positions)

    while queue:
        row, col, date = queue.popleft()
        answer_info[1] += 1

        if row > 0 and box[row-1][col] == 0:
            queue.append((row-1, col, date+1))
            box[row-1][col] = 1
        if row < N-1 and box[row+1][col] == 0:
            queue.append((row+1, col, date+1))
            box[row+1][col] = 1
        if col > 0 and box[row][col-1] == 0:
            queue.append((row, col-1, date+1))
            box[row][col-1] = 1
        if col < M-1 and box[row][col+1] == 0:
            queue.append((row, col+1, date+1))
            box[row][col+1] = 1
    
    return date


# M: 가로, N: 세로
M, N = map(int, read().split())
# box: 토마토 상태, riped_tomato: 익은 토마토들의 위치
box, riped_tomato,  = [], []
# answer_info: [토마토가 익기까지 최소 값, 체크한 위치 수]
answer_info = [0, 0]
for row in range(N):
    box.append(list(map(int, read().split())))
    for col in range(M):
        if box[row][col] == 1:
            riped_tomato.append((row, col, 0))
        elif box[row][col] == -1:
            answer_info[1] += 1

answer_info[0] = bfs(riped_tomato)
if answer_info[1] == M * N:
    print(answer_info[0])
else:
    print(-1)