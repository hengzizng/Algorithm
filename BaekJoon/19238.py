from collections import deque
import sys
read = sys.stdin.readline


def drive():
    drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue = deque([(taxi[0], taxi[1], 0)])
    visited = set([(taxi[0], taxi[1])])

    find_people = [] # 태울 승객의 위치 리스트
    find_dist = N * N # 처음으로 찾은 태울 승객의 거리
    while queue:
        row, col, dist = queue.popleft()

        # 만약 거리가 남은 연료보다 더 커졌다면 탐색 종료
        # 만약 승객을 찾았고, 이번에 탐색할 위치의 거리가 찾은 승객의 거리보다 멀다면 탐색 종료
        if dist > fuel[0] or dist > find_dist:
            break

        if 2 <= area[row][col] <= M + 1: # 태울 승객을 찾으면
            if find_dist == N * N: # 처음 만난 승객이면
                find_dist = dist
            find_people.append((row, col))

        for nr, nc in drdc:
            nr += row
            nc += col

            if 0 <= nr < N and 0 <= nc < N and area[nr][nc] != 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    if find_dist == N * N: # 태울 승객을 못찾았다면
        return False

    find_people.sort() # 행이 작고, 열이 작은 순으로 정렬
    
    # 태운 승객 1명의 좌표로 택시 위치 설정
    taxi[0] = find_people[0][0]
    taxi[1] = find_people[0][1]
    dest = destinations[area[taxi[0]][taxi[1]]] # 목적지 설정
    
    area[taxi[0]][taxi[1]] = 0 # 승객을 태우면 빈 자리로 설정
    fuel[0] -= find_dist # 사용한 연료를 빼준다.
    
    queue = deque([(taxi[0], taxi[1], 0)])
    visited = set([(taxi[0], taxi[1])])

    while queue:
        row, col, dist = queue.popleft()

        if dist > fuel[0]:
            return False

        if row == dest[0] and col == dest[1]: # 승객의 목적지를 찾으면 종료
            fuel[0] += dist # 사용한 연료를 빼고, 2배를 충전한다
            # 택시 위치 재설정
            taxi[0] = row
            taxi[1] = col
            return True

        for nr, nc in drdc:
            nr += row
            nc += col

            if 0 <= nr < N and 0 <= nc < N and area[nr][nc] != 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return False


# N: 지도 크기, M: 승객 수, fuel: 초기 연료
N, M, fuel = map(int, read().split())

fuel = [fuel]

area = [] # 지도
for _ in range(N):
    area.append(list(map(int, read().split()))) # 0은 빈 칸, 1은 벽

taxi = list(map(int, read().split())) # 시작 위치
# 인덱스를 맞춰주기 위해 1씩 뺀다
taxi[0] -= 1
taxi[1] -= 1

destinations = {}
for i in range(2, M + 2):
    # 각 승객의 출발지(2 ~ M + 1)를 지도에 표시
    depart_row, depart_col, dest_row, dest_col = map(int, read().split())
    area[depart_row - 1][depart_col - 1] = i
    # 각 승객의 도착지 좌표를 저장 (다른 승객의 출발지와 겹치는 경우가 존재한다.)
    destinations[i] = (dest_row - 1, dest_col - 1)

is_success = True
for _ in range(M):
    if not drive():
        is_success = False
        break

print(fuel[0] if is_success else -1)