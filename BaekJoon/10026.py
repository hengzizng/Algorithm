import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("TestCase/BaekJoon/10026input.txt")
read = sys.stdin.readline


def blueCheck(i, j):
    normal[i][j] = True
    abnormal[i][j] = True

    for dx, dy in dxdy:
        dx += i
        dy += j
        if 0 <= dx < N and 0 <= dy < N and not normal[dx][dy] and grid[dx][dy] == 'B':
            blueCheck(dx, dy)


def abnormalCheck(i, j):
    abnormal[i][j] = True

    for dx, dy in dxdy:
        dx += i
        dy += j
        if 0 <= dx < N and 0 <= dy < N:
            if not abnormal[dx][dy] and grid[dx][dy] != 'B':
                abnormalCheck(dx, dy)


def normalCheck(i, j, origin_color):
    normal[i][j] = True

    for dx, dy in dxdy:
        dx += i
        dy += j
        if 0 <= dx < N and 0 <= dy < N:
            if not normal[dx][dy] and grid[dx][dy] == origin_color:
                normalCheck(dx, dy, origin_color)


dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N = int(read())
normal = [[False] * N for _ in range(N)]
abnormal = [[False] * N for _ in range(N)]
grid = []
for _ in range(N):
    grid.append(list(read().strip()))

count = [0, 0]  # normal count, abnormal count
for i in range(N):
    for j in range(N):
        if normal[i][j]:  # 정상인 사람이 체크한 곳이면 색약인 사람도 체크했을 것
            continue

        if grid[i][j] == 'B':  # 파란색은 정상, 색약인 모두 체크해야한다.
            blueCheck(i, j)
            count[0] += 1
            count[1] += 1
        elif abnormal[i][j]:  # 색약만 체크한 곳이면
            normalCheck(i, j, grid[i][j])
            count[0] += 1
        else:  # 파란색이 아닌데 색약이 체크하지 않은 곳이면
            normalCheck(i, j, grid[i][j])
            abnormalCheck(i, j)
            count[0] += 1
            count[1] += 1

print(count[0], count[1])
