from collections import deque
import sys
read = sys.stdin.readline

direction = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]


def get_move_count(I, now, destination):
    queue = deque([(now[0], now[1], 0)])
    visited = set([(now[0], now[1], 0)])

    while queue:
        x, y, move_count = queue.popleft()
        if x == destination[0] and y == destination[1]:
            break

        for next_x, next_y in direction:
            next_x, next_y = next_x + x, next_y + y
            if (
                0 <= next_x < I and
                0 <= next_y < I and
                (next_x, next_y) not in visited
            ):
                visited.add((next_x, next_y))
                queue.append((next_x, next_y, move_count + 1))

    return move_count


test_count = int(read())
move_counts = []
for _ in range(test_count):
    # I: 체스판의 한 변의 길이
    I = int(read())
    now = list(map(int, read().split()))
    destination = list(map(int, read().split()))
    move_counts.append(get_move_count(I, now, destination))

for move_count in move_counts:
    print(move_count)