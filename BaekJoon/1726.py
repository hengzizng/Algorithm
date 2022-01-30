from collections import deque
from distutils import command
import sys
read = sys.stdin.readline

# 로봇 이동 명령
# 1. Go 1~3 : 현재 향하고 있는 방향으로 1~3만큼 간다
# 2. Turn left/right : 왼쪽/오른쪽 으로 회전

# 원하는 위치로 이동, 원하는 방향 보도록 하는데 최소 몇 번의 명령이 필요한지?
# 1: 동, 2: 서, 3: 남, 4: 북 으로 주어짐

# 동, 서, 남, 북 -> 북, 동, 남, 서 순으로 변경
def setDirection(origin):
    direction = -1

    if origin == 0: # 동쪽
        direction = 1
    elif origin == 1: # 서쪽
        direction = 3
    elif origin == 2: # 남쪽
        direction = 2
    elif origin == 3: # 북쪽
        direction = 0
    
    return direction

# now 방향에서 왼쪽으로 회전
def turn_left(now):
    return (now + 3) % 4

# now 방향에서 오른쪽으로 회전
def turn_right(now):
    return (now + 1) % 4

def get_min_command_count():
    queue = deque([(robot[0], robot[1], robot[2], 0)])
    command_count[robot[0]][robot[1]][robot[2]] = 0

    while queue:
        row, col, direction, count = queue.popleft()

        if row == destination[0] and col == destination[1] and direction == destination[2]:
            return
        
        # Turn left
        next_direction = turn_left(direction)
        if count + 1 < command_count[row][col][next_direction]:
            command_count[row][col][next_direction] = count + 1
            queue.append((row, col, next_direction, count + 1))
        
        # Turn right
        next_direction = turn_right(direction)
        if count + 1 < command_count[row][col][next_direction]:
            command_count[row][col][next_direction] = count + 1
            queue.append((row, col, next_direction, count + 1))

        # Go k
        for k in range(1, 3 + 1):
            next_row, next_col = row + (drdc[direction][0] * k), col + (drdc[direction][1] * k)

            if next_row < 0 or next_row >= M or next_col < 0 or next_col >= N or factory[next_row][next_col] == 1:
                break

            # 이 부분을 위의 break문에 넣으면 2 -> 3 -> 4 의 경우, 4를 갱신할 수 없다
            if count + 1 < command_count[next_row][next_col][direction]:
                command_count[next_row][next_col][direction] = count + 1
                queue.append((next_row, next_col, direction, count + 1))
    


# 북, 동, 남, 서
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# M: 행 수, N: 열 수
M, N = map(int, read().split())

# factory의 값 - 0: 로봇이 갈 수 O / 1: 로봇이 갈 수 X
factory = []
for _ in range(M):
    factory.append(list(map(int, read().split())))

# 로봇의 행 인덱스, 열 인덱스, 방향
robot = list(map(lambda x: int(x) - 1, read().split()))
destination = list(map(lambda x: int(x) - 1, read().split()))

# 동, 서, 남, 북 -> 북, 동, 남, 서 으로 변경
robot[2] = setDirection(robot[2])
destination[2] = setDirection(destination[2])

# 각 위치, 방향에 도착할 수 있는 최소 명령어 수
command_count = [[[float('inf')] * 4 for _ in range(N)] for _ in range(M)]

get_min_command_count()

print(command_count[destination[0]][destination[1]][destination[2]])