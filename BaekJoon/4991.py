from collections import deque
import sys
read = sys.stdin.readline


# 두 지점 간 최단 거리를 구한다.
def get_distance(depart, dest):
    queue = deque([(depart[0], depart[1], 0)])
    visited = set([(depart[0], depart[1])])

    while queue:
        r, c, distance = queue.popleft()

        for dr, dc in drdc:
            nr, nc = r + dr, c + dc

            if 0 <= nr < h and 0 <= nc < w and room[nr][nc] != 'x' and (nr, nc) not in visited:
                # 목적지에 갈 수 있는 경우 그 거리를 반환
                if nr == dest[0] and nc == dest[1]:
                    return distance + 1

                queue.append((nr, nc, distance + 1))
                visited.add((nr, nc))

    # 목적지에 갈 수 없는 경우 -1을 반환
    return -1


# 각 칸들 간 거리를 구한다.
def get_distances(locs):
    distances = [[-1] * loc_count for _ in range(loc_count)]
    for depart in range(loc_count):
        for dest in range(depart + 1, loc_count):
            distance = get_distance(locs[depart], locs[dest])
            # 방문할 수 없는 칸이 존재하면 더 이상 거리 구할 필요 X
            if distance == -1:
                return distance

            distances[depart][dest] = distances[dest][depart] = distance

    return distances


# 각 위치를 방문할 순서를 정하고, 이동 횟수를 구한다.
def set_order(count, before, move_count, is_visit):
    if min_move_count[0] < move_count:
        return

    if count == loc_count:
        min_move_count[0] = move_count
        return

    for i in range(loc_count):
        if not is_visit[i]:
            # 이번에 i 인덱스의 위치 방문
            is_visit[i] = True
            set_order(count + 1, i, move_count + distances[before][i], is_visit)
            is_visit[i] = False


loc_count = 0
min_move_count = [float('inf')]  # 이동 횟수의 최솟값
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while True:  # 테스트케이스 반복
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break

    room = [list(read().strip()) for _ in range(h)]

    min_move_count = [float('inf')]  # 이동 횟수의 최솟값
    targets = []  # 청소할 칸들의 위치
    robot = [-1, -1]  # 로봇 청소기의 위치
    for r in range(h):
        for c in range(w):
            if room[r][c] == 'o':
                robot = [r, c]
            elif room[r][c] == '*':
                targets.append([r, c])

    loc_count = len(targets) + 1

    # 로봇 청소기의 위치를 포함한 청소할 칸들 간 거리를 구한다.
    distances = get_distances([robot] + targets)

    # 방문할 수 없는 더러운 칸이 존재하는 경우
    if distances == -1:
        print(-1)
        continue

    # 각 위치를 방문할 순서 순열을 구하고 그 때의 이동 횟수를 구한다
    is_visit = [False] * loc_count
    is_visit[0] = True
    set_order(1, 0, 0, is_visit)

    # 이동 횟수 출력
    print(min_move_count[0])
