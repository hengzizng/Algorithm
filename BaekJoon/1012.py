from collections import deque
import sys
read = sys.stdin.readline


def get_area_count(M, N, cabbage):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    count = 0

    while cabbage:
        queue = deque([cabbage.pop()])
        while queue:
            x, y = queue.popleft()

            for next_x, next_y in direction:
                next_x, next_y = next_x + x, next_y + y
                if (
                    0 <= next_x < M and
                    0 <= next_y < N and
                    (next_x, next_y) in cabbage
                ):
                    cabbage.remove((next_x, next_y))
                    queue.append((next_x, next_y))
        count += 1
    
    return count


answers = []
T = int(read())
for _ in range(T):
    M, N, K = map(int, read().split())
    cabbage = set()
    
    for _ in range(K):
        X, Y = map(int, read().split())
        cabbage.add((X, Y))
    
    answers.append(get_area_count(M, N, cabbage))

for answer in answers:
    print(answer)
