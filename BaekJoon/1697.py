from collections import deque


def bfs(now_location, now_time):
    queue = deque([(now_location, now_time)])
    visited = {now_location}

    while queue:
        now_location, now_time = queue.popleft()
        if now_location == K:
            break

        if now_location - 1 >= 0 and now_location - 1 not in visited:
            queue.append((now_location - 1, now_time + 1))
            visited.add(now_location - 1)
        if now_location + 1 <= 100000 and now_location + 1 not in visited:
            queue.append((now_location + 1, now_time + 1))
            visited.add(now_location + 1)
        if now_location * 2 <= 100000 and now_location * 2 not in visited:
            queue.append((now_location * 2, now_time + 1))
            visited.add(now_location * 2)
    
    return now_time


# N: 현재 위치, K: 도착해야하는 위치
N, K = map(int, input().split())
print(bfs(N, 0))