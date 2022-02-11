from collections import deque
import sys
read = sys.stdin.readline


# 시계 방향으로 90도 회전시킨 뒤 전 세대의 끝점에 연결
def rotate(dots):
    new_dots = deque()
    for y, x in dots:
        # 순서 주의
        new_dots.appendleft((x, -y))

    diff_y = dots[-1][0] - new_dots[0][0]
    diff_x = dots[-1][1] - new_dots[0][1]

    for y, x in new_dots:
        dots.append((y + diff_y, x + diff_x))

    return dots


# 드래곤 커브에 표시를 해준다
def mark(no, dots):
    for y, x in dots:
        board[y][x] = no


# 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 구한다
def count_square():
    count = 0

    for y in range(100):
        for x in range(100):
            if board[y][x] != 0 and board[y + 1][x] != 0 and board[y][x + 1] != 0 and board[y + 1][x + 1] != 0:
                count += 1

    return count


dydx = [[0, 1], [-1, 0], [0, -1], [1, 0]]
board = [[0] * 101 for _ in range(101)]
N = int(read())  # 드래곤 커브의 개수
for n in range(1, N + 1):  # 드래곤 커브의 정보
    x, y, d, g = map(int, read().split())  # x,y: 시작 점, d: 시작 방향, g: 세대
    start = (y, x)  # 이번 드래곤 커브의 시작점

    dots = [(y, x), (y + dydx[d][0], x + dydx[d][1])]
    mark(n, dots)
    for _ in range(g):
        dots = rotate(dots)  # 이번에 새롭게 추가된 _세대 드래곤 커브를 포함한 위치들을 가져온다
        mark(n, dots)  # 드래곤 커브를 표시한다

print(count_square())
