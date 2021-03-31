from collections import deque
from sys import stdin


def bfs(start_nodes):
    queue = deque(start_nodes)

    if not queue:
        return -1

    while queue:
        width, depth, height, time = queue.popleft()
        warehouse[height][depth][width] = 1
        if width - 1 >= 0 and warehouse[height][depth][width-1] == 0:
            queue.append((width-1, depth, height, time+1))
            warehouse[height][depth][width-1] = 1
        if width + 1 < M and warehouse[height][depth][width+1] == 0:
            queue.append((width+1, depth, height, time+1))
            warehouse[height][depth][width+1] = 1
        if depth - 1 >= 0 and warehouse[height][depth-1][width] == 0:
            queue.append((width, depth-1, height, time+1))
            warehouse[height][depth-1][width] = 1
        if depth + 1 < N and warehouse[height][depth+1][width] == 0:
            queue.append((width, depth+1, height, time+1))
            warehouse[height][depth+1][width] = 1
        if height - 1 >= 0 and warehouse[height-1][depth][width] == 0:
            queue.append((width, depth, height-1, time+1))
            warehouse[height-1][depth][width] = 1
        if height + 1 < H and warehouse[height+1][depth][width] == 0:
            queue.append((width, depth, height+1, time+1))
            warehouse[height+1][depth][width] = 1
    
    for box in warehouse:
        for floor in box:
            if 0 in floor:
                return -1

    return time


# M: 가로, N: 세로, H: 높이
M, N, H = map(int, input().split())
warehouse, ripe = [], []
for height in range(H):
    box = []
    for depth in range(N):
        row = list(map(int, stdin.readline().strip().split()))
        box.append(row)
        for i in range(len(row)):
            if row[i] == 1:
                ripe.append((i, depth, height, 0))
    warehouse.append(box)

print(bfs(ripe))