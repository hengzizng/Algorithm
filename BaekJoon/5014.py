from collections import deque


def bfs(start_floor):
    queue = deque([(start_floor, 0)])
    visited = set([start_floor])

    while queue:
        now_floor, time = queue.popleft()
        if now_floor == G:
            return time

        if now_floor + U <= F and now_floor + U not in visited:
            queue.append((now_floor+U, time+1))
            visited.add(now_floor + U)
        if now_floor - D >= 1 and now_floor - D not in visited:
            queue.append((now_floor-D, time+1))
            visited.add(now_floor - D)
    
    return 'use the stairs'


# F: 건물 층 수, S: 출발지(현재) 층 수, G: 도착지(목표) 층 수
# U: 위로 이동 단위, D: 아래로 이동 단위
F, S, G, U, D = map(int, input().split())
print(bfs(S))