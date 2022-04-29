from collections import deque
import heapq
import sys
read = sys.stdin.readline


# S, 모든 K 간의 최소 거리를 구한다.
# 최소 거리 순으로 방문
#   이미 방문한 곳이라면 버린다
#   방문하지 않은 곳이라면 방문 체크
#   방문한 곳이 K 개수 + 1 이라면 탐색 종료

def find(loc):
    while loc != parents[loc]:
        parents[loc] = parents[parents[loc]]
        loc = parents[loc]
    return loc


def union(loc1, loc2):
    loc1 = find(loc1)
    loc2 = find(loc2)
    parents[loc1] = loc2


def set_distances_by_depart(depart_index):
    queue = deque([(0, locs[depart_index][0], locs[depart_index][1])])
    visited = set([(locs[depart_index][0], locs[depart_index][1])])

    while queue:
        distance, r, c = queue.popleft()

        for dr, dc in drdc:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited or miro[nr][nc] == 1:
                continue

            if miro[nr][nc] >= 2:
                heapq.heappush(
                    distances, (distance + 1, depart_index, miro[nr][nc] - 2)
                )

            visited.add((nr, nc))
            queue.append((distance + 1, nr, nc))


drdc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M = map(int, read().split())
miro = [list(read().strip()) for _ in range(N)]
locs = []  # 로봇의 시작 위치, 키들의 위치

# 시작 위치와 키들의 위치를 구한다.
for i in range(N):
    for j in range(N):
        if miro[i][j] == 'S' or miro[i][j] == 'K':
            miro[i][j] = str(len(locs) + 2)
            locs.append([i, j])
        miro[i][j] = int(miro[i][j])

# 각 위치들 간의 거리를 구한다. (BFS)
distances = []
for depart in range(M + 1):
    set_distances_by_depart(depart)

# 로봇이 움직인 횟수의 총 합의 최소를 구한다. (MST)
parents = list(range(M + 1))
total_distance = 0
found_key_count = 0
while distances:
    distance, loc1, loc2 = heapq.heappop(distances)

    if find(loc1) == find(loc2):
        continue

    union(loc1, loc2)
    total_distance += distance
    found_key_count += 1
    if found_key_count == M:
        break

print(total_distance if found_key_count == M else -1)
