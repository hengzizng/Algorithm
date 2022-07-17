from heapq import heappush, heappop
import sys
read = sys.stdin.readline


def is_valid(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


def get_min_time():
    # (시간, -행, -열, 오작교 추가 여부) 리스트 우선순위 큐 (최소시간 순)
    pq = [(0, 0, 0, 0)]
    # 방문체크 배열 [오작교 추가 없이 방문, 오작교 추가해서 방문]
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
    visited[0][0][0] = 1

    while pq:
        time, r, c, is_add = heappop(pq)
        r, c = r * -1, c * -1

        # 직녀에게 도착했다면
        if r == N - 1 and c == N - 1:
            return time

        for dr, dc in drdc:
            nr, nc = dr + r, dc + c

            # 이동할 수 없는 곳, 이미 방문했던 곳으로는 이동하지 않음
            if not is_valid(nr, nc) or area[nr][nc] == -1 or visited[nr][nc][is_add] == 1:
                continue

            # 다음으로 이동할 곳이 일반 땅일 경우
            if area[nr][nc] == 1:
                heappush(pq, (time + 1, nr * -1, nc * -1, is_add))
                visited[nr][nc][is_add] = 1
                continue

            # 다음으로 이동할 곳이 절벽(오작교)일 경우
            # 현재 위치가 절벽이라면(이번에 오작교를 이용했다면) 다음은 절벽으로 이동 불가
            if area[r][c] != 1:
                continue

            # 현재 위치가 절벽이 아닐 경우
            # 이미 만들어진 오작교이거나, 오작교를 추가한 적이 없어 오작교를 새로 만드는 경우
            if area[nr][nc] >= 2 or (area[nr][nc] == 0 and is_add == 0):
                new_is_add = 1 if area[nr][nc] == 0 else is_add

                # 주기를 이용해 건널 수 있는 시간을 찾는다.
                unit = M if area[nr][nc] == 0 else area[nr][nc]
                new_time = unit
                while new_time < time + 1:
                    new_time += unit
                heappush(pq, (new_time, nr * -1, nc * -1, new_is_add))
                visited[nr][nc][new_is_add] = 1


drdc = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하우상좌
N, M = map(int, read().split())
area = [list(map(int, read().split())) for _ in range(N)]

# 절벽이 교차해서 오작교를 놓을 수 없는 위치를 -1로 설정
for r in range(N):
    for c in range(N):
        # 절벽일 때 교차점인지 확인
        if area[r][c] == 0:
            count = 0
            # 네 방향을 확인해 비트로 표시
            for d in range(4):
                nr, nc = drdc[d][0] + r, drdc[d][1] + c
                if is_valid(nr, nc) and area[nr][nc] != 1:
                    count = count | (1 << d)
            # 교차점이면 표시
            # 교차점이 아닌 경우 : 0000 0001 0010 0100 1000 0101 1010
            if count not in {0, 1, 2, 4, 8, 5, 10}:
                area[r][c] = -1

print(get_min_time())
