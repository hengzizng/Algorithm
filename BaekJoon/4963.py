import sys
from collections import deque

sys.setrecursionlimit(10**6)
read = sys.stdin.readline


def dfs_recursion(row, col, height, width, now_map):
    now_map[row][col] = 0
    for i, j in next_positions:
        if 0 <= row+i < height and \
           0 <= col+j < width and \
           now_map[row+i][col+j] == 1:
            dfs(row+i, col+j, height, width, now_map)
    

def dfs_stack(row, col, height, width, now_map):
    stack = deque([(row, col)])

    while stack:
        row, col = stack.pop()
        if 0 <= row < height and \
           0 <= col < width and \
           now_map[row][col] == 1:
            now_map[row][col] = 0
            for i, j in next_positions:
                stack.append((row + i, col + j))


next_positions = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                  (1, 1), (1, 0), (1, -1), (0, -1)]


counts = []
# w: 지도의 너비, h: 지도의 높이
w, h = map(int, read().split())
while w != 0 and h != 0:
    # now_map: 지도
    now_map = []
    for _ in range(h):
        now_map.append(list(map(int, read().split())))

    count = 0
    for row in range(h):
        for col in range(w):
            if now_map[row][col] == 1:
                dfs_stack(row, col, h, w, now_map)
                # dfs_recursion(row, col, h, w, now_map)
                count += 1
    counts.append(count)

    w, h = map(int, read().split())


for count in counts:
    print(count)