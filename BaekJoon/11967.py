from collections import defaultdict, deque
import sys
read = sys.stdin.readline


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# N: 헛간의 크기, M: 스위치 정보 개수
N, M = map(int, read().split())
# switches[(x, y)]: (x, y)에서 불을 켤 수 있는 방 리스트
switches = defaultdict(list)
for _ in range(M):
    x, y, a, b = map(int, read().split())
    switches[(x - 1, y - 1)].append((a - 1, b - 1))
# 불이 켜져있는지 여부
on_rooms = [[0] * N for _ in range(N)]
# 베시가 갈 수 있는지 여부
go_rooms = [[0] * N for _ in range(N)]

# 갈 수 있는 방들에서 BFS를 위한 큐
queue = deque([(0, 0)])
on_rooms[0][0] = 1
go_rooms[0][0] = 1
on_count = 1
while queue:
    now_room = queue.popleft()

    # 현재 방에서 불을 켤 수 있는 방
    for next_room in switches[now_room]:
        # 불이 이미 켜져있다면 확인 필요 X
        if on_rooms[next_room[0]][next_room[1]] == 1:
            continue

        on_rooms[next_room[0]][next_room[1]] = 1
        on_count += 1

        # 불을 켠 방으로 갈 수 있다면 queue에 추가
        for nr, nc in drdc:
            nr, nc = next_room[0] + nr, next_room[1] + nc
            if 0 <= nr < N and 0 <= nc < N and go_rooms[nr][nc] == 1:
                queue.append(next_room)
                go_rooms[next_room[0]][next_room[1]] = 1
                break

    # 현재 방에서 갈 수 있는 방을 큐에 추가
    for nr, nc in drdc:
        nr, nc = now_room[0] + nr, now_room[1] + nc
        if 0 <= nr < N and 0 <= nc < N and on_rooms[nr][nc] == 1 and go_rooms[nr][nc] == 0:
            queue.append((nr, nc))
            go_rooms[nr][nc] = 1

print(on_count)
