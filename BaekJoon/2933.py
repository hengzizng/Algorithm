from collections import deque
import sys
read = sys.stdin.readline


# 클러스터가 value만큼 떨어진다
def drop(value, cluster):
    # 클러스터가 value만큼 떨어질 수 있는지 여부
    is_valid = True
    for r, c in cluster:
        if r + value >= R or cave[r + value][c] == 'x':
            is_valid = False
            break

    return is_valid


# 클러스터를 탐색하고, 탐색한 자리를 빈 칸으로 만듦
def get_cluster(r, c):
    # 클러스터 탐색을 시작하려는 위치가 미네랄일 경우에만 탐색 시작
    if r < 0 or r >= R or c < 0 or c >= C or cave[r][c] == '.':
        return set()

    cave[r][c] = '.'
    queue = deque([(r, c)])
    visited = set([(r, c)])

    while queue:
        r, c = queue.popleft()

        for dr, dc in drdc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and (nr, nc) not in visited:
                cave[nr][nc] = '.'
                queue.append((nr, nc))
                visited.add((nr, nc))

    return visited


# direction: 막대를 던질 방향 (1 [->], -1 [<-])
def shoot(direction, r):
    c = 0 if direction == 1 else C - 1
    while 0 <= c < C:
        if cave[r][c] == 'x':
            cave[r][c] = '.'
            break
        c += direction

    return r, c


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# R: 행 수, C: 열 수
R, C = map(int, read().split())
# cave: 동굴 상태
cave = [list(read().strip()) for _ in range(R)]
# N: 막대를 던진 횟수
N = int(read())
# heights: 막대를 던진 높이(행) 리스트
heights = list(map(lambda x: R - int(x), read().split()))
# direction: 막대를 던질 방향 (1 [->], -1 [<-])
direction = -1
for height in heights:
    direction *= -1

    # 파괴된 미네랄의 위치
    destroy_r, destroy_c = shoot(direction, height)

    # 미네랄이 파괴되었을 경우에만 클러스터 탐색
    if destroy_c == -1 or destroy_c == C:
        continue

    # 파괴된 미네랄과 인접한 클러스터 탐색
    for dr, dc in drdc:
        nr, nc = destroy_r + dr, destroy_c + dc
        cluster = get_cluster(nr, nc)
        # 클러스터가 존재할 경우 떨어짐
        if cluster:
            # 클러스터가 떨어질 높이
            drop_height = 0
            for value in range(1, R):
                if drop(value, cluster):
                    drop_height = value
                else:
                    break

            # 클러스터를 탐색하면서 빈 칸으로 만들었기 때문에 다시 채워줌
            for r, c in cluster:
                cave[r + drop_height][c] = 'x'

            # 동시에 떨어지는 클러스터는 없기 때문에 현재 클러스터가 떨어졌다면 클러스터 탐색 종료
            if drop_height > 0:
                break

for r in range(R):
    print(''.join(cave[r]))
