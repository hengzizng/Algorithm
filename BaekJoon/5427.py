import sys
from collections import deque


# bfs: 1초단위의 bfs
# mode: 0(person), 1(fire)
def bfs(mode, queue, building, height, width):
    for _ in range(len(queue)):
        row, col = queue.popleft()

        # 사람이 출구 도착 시 1 반환
        if mode == 0:
            if (
                row == 0 or row == height - 1 or
                col == 0 or col == width - 1
            ):
                return 1
        
        for x, y in next_movement:
            x, y = row + x, col + y
            if mode == 0:
                if (
                    0 <= x < height and 0 <= y < width and
                    building[x][y] == '.'
                   ):
                    queue.append((x, y))
                    building[x][y] = '@'
            else:
                if (
                    0 <= x < height and 0 <= y < width and
                    building[x][y] != '#' and building[x][y] != '*'
                   ):
                    queue.append((x, y))
                    building[x][y] = '*'
    
    return 0


def find_exit(building, height, width, person, fire):
    time = 0
    person_queue = deque([(person[0], person[1])])
    fire_queue = deque(fire)

    while person_queue:
        result = bfs(1, fire_queue, building, height, width)
        result = bfs(0, person_queue, building, height, width)
        if result == 1:
            return time + 1
        time += 1
        
    return 'IMPOSSIBLE'


# 아래 find_exit 함수를 find_exit 함수와 bfs 함수로 분리
'''
def find_exit(building, height, width, person, fire):
    before_time, time = -1, 0
    person_queue = deque([(person[0], person[1], time)])
    fire_queue = deque(fire)

    while person_queue:
        row, col, time = person_queue.popleft()

        # 상근이가 이동하면 불도 옮긴다.
        if before_time < time:
            for _ in range(len(fire_queue)):
                fire_row, fire_col = fire_queue.popleft()
                for x, y in next_movement:
                    x, y = fire_row + x, fire_col + y
                    if (
                        0 <= x < height and 0 <= y < width and
                        building[x][y] != '#' and building[x][y] != '*'
                    ):
                        fire_queue.append((x, y))
                        building[x][y] = '*'
        
        if (
            row == 0 or row == height - 1 or
            col == 0 or col == width - 1
        ):
            return time + 1
        
        for x, y in next_movement:
            x, y = row + x, col + y
            if (
                0 <= x < height and 0 <= y < width and
                building[x][y] == '.'
            ):
                person_queue.append((x, y, time+1))
                building[x][y] = '@'
        
        before_time = time

    return 'IMPOSSIBLE'
'''


next_movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]
read = sys.stdin.readline

answers = []
test_num = int(read())
for _ in range(test_num):
    # building: 건물 지도, person: 상근이 위치, fire: 불 위치
    building, person, fire = [], [-1, -1], []
    w, h = map(int, read().split())
    for row in range(h):
        floor = read().strip()
        for col in range(w):
            if floor[col] == '@':
                person = [row, col]
            elif floor[col] == '*':
                fire.append((row, col))
        building.append(list(floor))
    
    exit_time = find_exit(building, h, w, person, fire)
    answers.append(exit_time)

for answer in answers:
    print(answer)