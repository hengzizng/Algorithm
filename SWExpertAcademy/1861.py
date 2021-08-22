# 64,644 kb
# 메모리
# 1,218 ms
# 실행시간
# 1,197
# 코드길이

from collections import deque
import sys
sys.stdin = open("SWExpertAcademy/1861input.txt")

def dfs(row, col):
    stack = deque()
    stack.append((row, col, 1))

    while stack:
        x, y, count = stack.pop()

        for dx, dy in dxdy:
            dx += x
            dy += y
            if 0 <= dx < N and 0 <= dy < N and rooms[dx][dy] == rooms[x][y] + 1:
                if counts[dx][dy] > 0:
                    counts[x][y] = counts[dx][dy] + 1
                    return counts[x][y]
                else:
                    stack.append((dx, dy, count + 1))

    counts[row][col] = count
    return count

dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    counts = [[0] * N for _ in range(N)]
    rooms = []
    for r in range(N):
        rooms.append(list(map(int, input().split())))

    max_count = -1
    room_no = 0
    for r in range(N):
        for c in range(N):
            now_count = dfs(r, c)
            if max_count < now_count:
                room_no = rooms[r][c]
                max_count = now_count
            elif max_count == now_count:
                room_no = min(room_no, rooms[r][c])

    print('#' + str(tc) + " " + str(room_no) + " " + str(max_count))

## 다른 solution
# 60,904 kb
# 214 ms
# 855

# dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# result = []
# for tc in range(1, 1 + int(input())):
#     N = int(input())
#     A = [list(map(int, input().split())) for _ in range(N)]
#     n = N ** 2 + 1
#     visited = [0] * n
#     for x in range(N):
#         for y in range(N):
#             for dx, dy in dxy:
#                 nx = x + dx
#                 ny = y + dy
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if A[x][y] + 1 == A[nx][ny]:
#                         visited[A[x][y]] = 1
#     start = length = 1
#     res = []
#     res1 = 0
#     res2 = 0
#     for i in range(1, n):
#         if visited[i]:
#             length += 1
#         else:
#             if length > res2:
#                 res2 = length
#                 res1 = start
#             length = 1
#             start = i + 1
#
#     result.append('#%d %d %d' % (tc, res1, res2))
#
# print('\n'.join(result))