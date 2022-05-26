import sys
read = sys.stdin.readline


# 두 위치 사이의 거리(시간)을 반환
def get_time(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def move(x, y, time):
    if time >= min_time[0]:
        return

    if x == xe and y == ye:
        min_time[0] = time
        return

    # 현재 위치에서 바로 도착 지점으로 이동
    move(xe, ye, time + get_time(x, y, xe, ye))

    # 현재 위치에서 텔레포트로 이동 (현재 위치 -> 텔레포트 시작점 -> 텔레포트 도착점)
    for next_loc in teleport.keys():
        if not is_visit[next_loc]:
            is_visit[next_loc] = True
            move(*teleport[next_loc], get_time(x, y, *next_loc) + time + 10)
            is_visit[next_loc] = False


# (xs, ys) -> (xe, ye)
xs, ys = map(int, read().split())  # 출발지
xe, ye = map(int, read().split())  # 도착지
teleport = {}  # 텔레포트
is_visit = {}  # 텔레포트 방문 여부
for _ in range(3):
    x1, y1, x2, y2 = map(int, read().split())
    teleport[(x1, y1)] = (x2, y2)
    teleport[(x2, y2)] = (x1, y1)
    is_visit[(x1, y1)] = False
    is_visit[(x2, y2)] = False

min_time = [get_time(xs, ys, xe, ye)]  # 집에 가는 가장 빠른 시간
move(xs, ys, 0)
print(min_time[0])
