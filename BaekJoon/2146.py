import sys
from collections import deque


def get_island(row, col, island_no):
    # island_no는 2부터 시작
    island_no += 2
    queue = deque([(row, col)])
    land[row][col] = island_no
    # island_list: [(섬의 행, 섬의 열, 섬까지의 거리), ...]
    island_list = [(row, col, 0)]

    while queue:
        row, col = queue.popleft()

        if row > 0 and land[row-1][col] == 1:
            queue.append((row-1, col))
            land[row-1][col] = island_no
            island_list.append((row-1, col, 0))
        if row < N-1 and land[row+1][col] == 1:
            queue.append((row+1, col))
            land[row+1][col] = island_no
            island_list.append((row+1, col, 0))
        if col > 0 and land[row][col-1] == 1:
            queue.append((row, col-1))
            land[row][col-1] = island_no
            island_list.append((row, col-1, 0))
        if col < N-1 and land[row][col+1] == 1:
            queue.append((row, col+1))
            land[row][col+1] = island_no
            island_list.append((row, col+1, 0))

    return island_list


def get_bridge_length(island_list, island_no):
    island_no += 2
    queue = deque(island_list)

    is_checked = set()
    for row, col, distance in island_list:
        is_checked.add((row, col))

    while queue:
        row, col, distance = queue.popleft()

        for x, y in next_movement:
            x, y = row + x, col + y
            if 0 <= x < N and 0 <= y < N and (x, y) not in is_checked:
                if land[x][y] not in checked_islands and land[x][y] > 0:
                    return distance
                elif land[x][y] == 0:
                    queue.append((x, y, distance+1))
                    is_checked.add((x, y))
    return float('inf')


read = sys.stdin.readline
next_movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# N: 지도의 크기
N = int(read())
# land: 지도
land = []
for _ in range(N):
    land.append(list(map(int, read().split())))

# count: 섬의 개수
count = 0
# min_bridge: 최소 거리
min_bridge = float('inf')
# checked_islands: 거리를 체크한 섬
checked_islands = set()
for row in range(N):
    for col in range(N):
        if land[row][col] == 1:
            island_list = get_island(row, col, count)
            checked_islands.add(count+2)
            min_bridge = min(min_bridge, get_bridge_length(island_list, count))
            count += 1

print(min_bridge)