from collections import deque
import sys

sys.stdin = open("BaekJoon/10026.txt")
read = sys.stdin.readline

def blueCheck(i, j):
    normal[i][j] = True
    abnormal[i][j] = True

    for dx, dy in dxdy:
        dx += i
        dy += j
        if 0 <= dx < N and 0 <= dy < N and not normal[dx][dy] and grid[dx][dy] == 'B':
            blueCheck(dx, dy)

def check(i, j, origin_color):
    print(">>>>>>>>", origin_color)
    stack = deque([(i, j)])

    while stack:
        print(stack)
        i, j = stack.pop()
        if grid[i][j] == origin_color:
            normal[i][j] = True
        abnormal[i][j] = True

        for dx, dy in dxdy:
            dx += i
            dy += j
            if 0 <= dx < N and 0 <= dy < N:
                if not normal[dx][dy] and grid[dx][dy] == origin_color:
                    stack.append((dx, dy))
                if not abnormal[dx][dy] and grid[dx][dy] != 'B':
                    stack.append((dx, dy))


dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N = int(read())
normal = [[False] * N for _ in range(N)]
abnormal = [[False] * N for _ in range(N)]
grid = []
for _ in range(N):
    grid.append(list(read().strip()))

count = [0, 0] # normal count, abnormal count
for i in range(N):
    for j in range(N):
        print(normal[i][j])
        if normal[i][j]:
            continue
        
        print(abnormal[i][j], i, j)
        if abnormal[i][j]:
            check(i, j, grid[i][j])
            count[0] += 1
        elif grid[i][j] == 'B':
            blueCheck(i, j)
            count[0] += 1
            count[1] += 1
        else:
            check(i, j, grid[i][j])
            count[0] += 1
            count[1] += 1

print(count[0], count[1])