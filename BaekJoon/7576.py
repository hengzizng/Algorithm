import sys
from collections import deque

read = sys.stdin.readline


def make_ripe(riped_tomato, answer_info):
    queue = deque(riped_tomato)

    while queue:
        row, col, time = queue.popleft()
        answer_info[1] += 1
        
        for x, y in next_position:
            x, y = row + x, col + y
            if 0 <= x < N and 0 <= y < M and box[x][y] == 0:
                queue.append((x, y, time + 1))
                box[x][y] = 1
    
    return time


next_position = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# M: 가로, N: 세로
M, N = map(int, read().split())
# box: 토마토 상태, riped_tomato: 익은 토마토들의 위치
box, riped_tomato = [], []
# answer_info: [토마토가 익기까지 최소 날짜, 체크한 위치 수]
answer_info = [-1, 0]
for row in range(N):
    box.append(list(map(int, read().split())))
    for col in range(M):
        if box[row][col] == 1:
            riped_tomato.append((row, col, 0))
        elif box[row][col] == -1:
            answer_info[1] += 1

if riped_tomato:
    answer_info[0] = make_ripe(riped_tomato, answer_info)
    if answer_info[1] < M * N:
        answer_info[0] = -1

print(answer_info[0])