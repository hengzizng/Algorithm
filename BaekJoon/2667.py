from collections import deque
from sys import stdin


def dfs(row, col):
    stack = deque()
    visited = set()
    stack.append((row, col))
    while stack:
        row, col = stack.pop()
        if row-1 >= 0 and matrix_map[row-1][col] == 1:
            stack.append((row-1, col))
        if row+1 <= N-1 and matrix_map[row+1][col] == 1:
            stack.append((row+1, col))
        if col-1 >= 0 and matrix_map[row][col-1] == 1:
            stack.append((row, col-1))
        if col+1 <= N-1 and matrix_map[row][col+1] == 1:
            stack.append((row, col+1))
        
        visited.add((row, col))
        matrix_map[row][col] = 0

    return len(visited)


matrix_map = []
N = int(input())
for i in range(N):
    matrix_map.append(list(map(int, stdin.readline().strip())))

answer = []
for row in range(N):
    for col in range(N):
        if matrix_map[row][col] == 1:
            answer.append(dfs(row, col))

print(len(answer))
answer.sort()
for apartment_complex in answer:
    print(apartment_complex)