from collections import deque
import sys
read = sys.stdin.readline


# 각 방을 탐색하고, 그 넓이를 저장
def search(r, c, room_no):
    queue = deque([(r, c)])
    room[r][c] = room_no
    count = 1

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            # 벽이 없으면 갈 수 있다.
            nr, nc = r + drdc[d][0], c + drdc[d][1]
            if (castle[r][c] & (1 << d)) == 0 and room[nr][nc] == -1:
                queue.append((nr, nc))
                room[nr][nc] = room_no
                count += 1

    areas.append(count)


# 인접한 방 목록을 구한다.
def get_adjust_rooms(r, c, room_no):
    queue = deque([(r, c)])
    visited = set([(r, c)])
    adjust_rooms = set()

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + drdc[d][0], c + drdc[d][1]
            if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in visited:
                # 벽이 없거나 같은 방이라면
                if (castle[r][c] & (1 << d)) == 0 or room[nr][nc] == room_no:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                # 벽이 있다면
                else:
                    adjust_rooms.add(room[nr][nc])

    adjust_list.append(adjust_rooms)


# 방향 벡터 (서북동남)
drdc = [[0, -1], [-1, 0], [0, 1], [1, 0]]
# N: 가로 길이(열 수), M: 성의 세로 길이(행 수)
N, M = map(int, read().split())
# 1 << (0123(서북동남)) 의 비트가 1일 경우 성곽이 있음
castle = [list(map(int, read().split())) for _ in range(M)]
# 각 방별로 인접한 방 리스트
adjust_list = []
# 각 방의 넓이
areas = []
# 각 위치별 속한 방 번호
room = [[-1] * N for _ in range(M)]

# 각 방을 탐색
room_no = 0
for r in range(M):
    for c in range(N):
        if room[r][c] == -1:
            search(r, c, room_no)
            room_no += 1

# 각 방별로 인접한 방들을 탐색
room_no = 0
for r in range(M):
    for c in range(N):
        if room[r][c] == room_no:
            get_adjust_rooms(r, c, room_no)
            room_no += 1

# 하나의 벽을 제거해서 얻을 수 있는 가장 넓은 방의 크기를 구한다.
max_sum_area = 0
for room1 in range(len(areas)):
    for room2 in adjust_list[room1]:
        max_sum_area = max(max_sum_area, areas[room1] + areas[room2])

print(len(areas))
print(max(areas))
print(max_sum_area)
