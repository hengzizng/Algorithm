from collections import deque
import sys
read = sys.stdin.readline


# 바이러스를 놓을 위치를 선택(M군데)
def select_virus(start, selected):
    # M개의 바이러스를 놓을 위치를 모두 선택했다면 종료
    if len(selected) == M:
        min_time[0] = min(min_time[0], get_spread_time(selected))
        return
    # 더이상 선택할 바이러스가 없을 경우
    if start == len(virus_list) or M - len(selected) > len(virus_list) - start:
        return
    
    for i in range(start, len(virus_list)):
        temp = virus_list[i]
        # i번째 바이러스를 실제로 놓음
        if temp not in selected:
            selected.add(temp)
            select_virus(i + 1, selected)
            selected.discard(temp)


# 선택된 위치 기반 바이러스가 모든 칸에 퍼지는 시간을 반환
def get_spread_time(selected):
    queue = deque()
    visited = set()
    total_time = 0

    for r, c in selected:
        queue.append((0, r, c))
        visited.add((r, c))

    while queue:
        time, r, c = queue.popleft()
        total_time = time

        for nr, nc in drdc:
            nr += r
            nc += c
            if 0 <= nr < N and 0 <= nc < N and lab[nr][nc] != 1 and (nr, nc) not in visited:
                queue.append((time + 1, nr, nc))
                visited.add((nr, nc))

    return total_time if len(visited) == empty_count else float('inf')


# 상하좌우 단위벡터
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# N: 연구소 크기 / M: 바이러스 개수
N, M = map(int, read().split(" "))

# 연구소에 바이러스가 존재할 수 있는 칸의 수
empty_count = 0
# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간
min_time = [float('inf')]
# 바이러스를 놓을 수 있는 위치 리스트
virus_list = []

# lab: 연구소 상태
# 0: 빈 칸 / 1: 벽 / 2: 바이러스를 놓을 수 있는 위치
lab = []
for r in range(N):
    lab.append(list(map(int, read().split())) )
    for c in range(N):
        if lab[r][c] == 1:
            continue
        empty_count += 1
        if lab[r][c] == 2:
            virus_list.append((r, c))

# 바이러스를 놓을 위치를 선택(M군데)
select_virus(0, set())

# 최소시간 출력
print(-1 if min_time[0] == float('inf') else min_time[0])