from heapq import heappush, heappop
import sys
read = sys.stdin.readline


def move():
    queue = [(0, 1)]
    visited = [0] * 101

    while queue:
        count, now = heappop(queue)

        # 100번 칸에 도착했다면
        if now == 100:
            return count

        # 사다리나 뱀으로 이동 가능할 경우
        if now in move_info:
            heappush(queue, (count, move_info[now]))
            continue
        # 주사위를 굴려서 이동
        for n in range(now + 1, min(100, now + 6) + 1):
            if visited[n] == 0:
                heappush(queue, (count + 1, n))
                visited[n] = 1

    # 여기까지 도착 X
    return 100


# N: 사다리 수, M: 뱀 수
N, M = map(int, read().split())

# 사다리, 뱀 정보 입력
move_info = {}
for _ in range(N + M):
    # i번 칸 -> j번 칸으로 이동
    i, j = map(int, read().split())
    move_info[i] = j

print(move())
