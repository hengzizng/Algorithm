from collections import deque
from sys import stdin


def dfs(row, col, benchmark):
    stack = deque([(row, col)])

    while stack:
        row, col = stack.pop()
        if row < 0 or row > N-1 or \
           col < 0 or col > N-1 or \
           matrix[row][col] <= benchmark:
            continue
        matrix[row][col] = benchmark
        stack.append((row-1, col))
        stack.append((row+1, col))
        stack.append((row, col-1))
        stack.append((row, col+1))


# N: 지역의 가로, 세로 길이
N = int(input())
matrix = []
min_height, max_height = 100, 1
for i in range(N):
    flattend_row = list(map(int, stdin.readline().strip().split()))
    matrix.append(flattend_row)
    min_height = min(min_height, min(flattend_row))
    max_height = max(max_height, max(flattend_row))

max_area_num = 0
# benchmark가 max_height일 때는 area_num = 0이므로 max_height-1부터 시작
for benchmark in range(max_height-1, (min_height-1)-1, -1):
    area_num = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > benchmark:
                dfs(i, j, benchmark)
                area_num += 1
    max_area_num = max(max_area_num, area_num)
print(max_area_num)