# N: 땅의 가로, 세로 크기
# A: 각 나라에 살고 있는 인원 수

# 인구 이동
# 1. L <= 인접한 두 나라의 인구 차이 <= R 라면 국경선을 오늘 하루 연다
# 2. 연합을 이루는 각 칸의 인구 수 = int(연합 내 총 인구 수 / 연합 내 나라의 수)
# 3. 인구 이동이 없을 때까지 반복

# 인구 이동이 몇일 동안 발생하는지?

# ======================

# bfs로 모든 나라 탐색 (area가 0인 곳이면 탐색 시작)
#   area_count += 1
#   area에 각 나라의 연합 번호(1 ~ )를 표시하면서 총 인구 수, 나라 수를 구한다
#   area에 따라 populations를 변경
# 인구 이동이 없다면(area_count == N * N) 인구 이동 종료
# -> 시간 초과
# ---------------------
# bfs로 모든 나라 탐색 (visited에 담겨지지 않은 곳이면 탐색 시작)
#   now_area와 visited에 각 나라의 위치를 담으면서 총 인구 수를 구한다
#   now_area를 돌면서 새로운 인구 수로 설정해준다
# 인구 이동이 없다면(area_count == N * N) 인구 이동 종료
# -> 시간 초과
# ---------------------
# visited를 2차원 배열로 변경
# -> 시간 초과
# ---------------------
# bfs로 (0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), ... 위치를 visit에 담아 탐색
#   : 한칸씩 건너 뛰더라도 연합이면 무조건 탐색이 이루어진다
#   visited에 date를 담아 이번에 탐색한 곳이면 건너 뛴다
#   연합인 곳만 다시 visit에 담는다 (이미 연합이 아니었던 곳끼리는 다음에도 연합이 아니다)
#   이번에 찾은 연합에 위치한 나라들에 새로운 인구 수를 저장한다
#   처음에 visit에 담았던 위치들을 다 탐색하고 난 뒤에 visit이 비어 있다면(인구 이동 발생 X) 종료


from collections import deque
import sys
read = sys.stdin.readline


# 각 연합을 찾고 인구를 재설정해준다
def set_populations(r, c, date):
    queue = deque([(r, c)])  # bfs를 위한 큐
    population = populations[r][c]  # 이번에 확인할 연합의 총 인구 수
    now_area = deque()  # 이번에 확인할 연합 내 나라 위치들
    visited[r][c] = date

    while queue:
        r, c = queue.popleft()
        now_area.append((r, c))

        for nr, nc in drdc:
            nr, nc = nr + r, nc + c

            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] == date:
                continue

            if L <= abs(populations[r][c] - populations[nr][nc]) <= R:
                population += populations[nr][nc]
                visited[nr][nc] = date
                queue.append((nr, nc))

    if len(now_area) > 1:  # 연합이 있을 때만 처리해준다
        new_population = population // len(now_area)
        while now_area:
            r, c = now_area.popleft()
            populations[r][c] = new_population
            visit.append((r, c))


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# N: 땅의 가로/세로 크기, L: 두 나라 최소 인구 차이, R: 두 나라 최대 인구 차이
N, L, R = map(int, read().split())
# populations: 각 나라의 인구 수
populations = [list(map(int, read().split())) for _ in range(N)]
# 이번 날짜에 확인했는지 여부
visited = [[-1] * N for _ in range(N)]
# 앞으로 확인할 위치들
visit = deque([(r, c) for r in range(N) for c in range(r % 2, N, 2)])
# date는 2000을 초과하지 않는다
for date in range(2000 + 1):
    # 이번 날짜에 확인할 위치들을 확인한다
    for _ in range(len(visit)):
        r, c = visit.popleft()
        # 이번 날짜에 이미 연합이 이루어졌으면 확인할 필요 없다
        if visited[r][c] != date:
            set_populations(r, c, date)

    # 더 이상 확인할 위치가 없다면 종료
    if not visit:
        print(date)
        break
