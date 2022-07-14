from collections import deque
import sys
read = sys.stdin.readline


def print_cave():
    for r in range(R):
        print(''.join(cave[r]))


# (r, c)의 위치에 미네랄이 있는지 여부 판단
# -1: 유효하지 않은 범위, 0: 미네랄 없음, 1: 미네랄 있음
def is_mineral(r, c):
    if 0 <= r < R and 0 <= c < C:
        if cave[r][c] == 'x':
            return 1
        else:
            return 0
    return -1


# 미네랄을 파괴하고, 그 열을 반환 (파괴하지 않았다면 -1 반환)
# r: 미네랄을 파괴할 행
# d: 방향 (0: <- (좌), 1: -> (우))
def destroy(r, d):
    c = 0 if d == 1 else C - 1

    while 0 <= c < C:
        if cave[r][c] == 'x':
            cave[r][c] = '.'
            return c
        c += drdc[d][1]

    # 파괴한 미네랄이 없다면
    return -1


# 바닥으로 떨어질 클러스터의 위치들을 반환
def get_drop_cluster(r, c):
    queue = deque([(r, c)])
    visited = set([(r, c)])
    # 가장 아래에 있는 미네랄의 행 위치
    max_r = r

    # BFS로 클러스터 탐색
    while queue:
        r, c = queue.popleft()
        max_r = max(r, max_r)

        for dr, dc in drdc:
            nr, nc = r + dr, c + dc
            if is_mineral(nr, nc) == 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
                # 클러스터가 바닥에 붙어있다면 빈 리스트 반환
                if nr == R - 1:
                    return R, []

    # 바닥에 있는 미네랄이 없다면 클러스터의 모든 위치 반환
    return max_r, list(visited)


# 클러스터를 한 칸 아래로 떨어뜨린다.
# 떨어졌으면 클러스터의 위치 리스트, 떨어지지 않았으면 빈 리스트 반환
def drop(cluster):
    can_drop = True
    moved = []

    # cave에서 지우면서 떨어질 위치를 moved에 담는다
    for _ in range(len(cluster)):
        r, c = cluster.pop()
        cave[r][c] = '.'
        moved.append((r + 1, c))

    # 떨어질 수 있는지 먼저 판단
    for r, c in moved:
        # 떨어지려는 칸에 미네랄이 있으면 떨어지지 않음
        if cave[r][c] == 'x':
            can_drop = False
            break

    # 떨어질 수 있으면
    if can_drop:
        for r, c in moved:
            cave[r][c] = 'x'
        return moved
    # 떨어질 수 없으면
    else:
        for r, c in moved:
            cave[r - 1][c] = 'x'
        return []


# 방향 벡터 (좌우상하)
drdc = [[0, -1], [0, 1], [-1, 0], [1, 0]]
# 동굴 정보
R, C = map(int, read().split())
cave = [list(read().strip()) for _ in range(R)]
# 던진 막대 수
N = int(read())
# 던진 막대의 행 위치 (높이 -> 행 정보로 변환)
sticks = list(map(lambda x: R - int(x), read().split()))

# 막대를 던질 방향 (0: <- (좌), 1: -> (우))
d = 1
for r in sticks:
    # 막대를 던진다
    c = destroy(r, d)
    d = (d + 1) % 2

    # 파괴된 미네랄이 없다면 클러스터가 분리되었는지 확인 X
    if c == -1:
        continue

    # 클러스터가 분리되었는지 여부 확인
    for dr, dc in drdc:
        # 파괴된 미네랄 주변에 미네랄이 있다면 클러스터가 바닥에 붙어있는지 확인
        nr, nc = r + dr, c + dc
        if is_mineral(nr, nc) == 1:
            max_r, cluster = get_drop_cluster(nr, nc)

            # 떨어질 클러스터가 아니라면
            if max_r == R:
                continue

            # 떨어질 클러스터가 있다면 떨어질 수 있을때까지 떨어뜨린 후 파괴된 미네랄 주변 탐색 종료
            for i in range(R - max_r - 1):
                cluster = drop(cluster)
                if not cluster:
                    break
            break

print_cave()
