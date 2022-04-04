from collections import deque
import sys
from types import new_class

read = sys.stdin.readline


def get_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def can_go(home, stores, festival):
    if get_distance(festival, home) <= (20 * 50):
        return "happy"

    visited = set()
    queue = deque([home])

    while queue:
        now = queue.popleft()

        if get_distance(now, festival) <= (20 * 50):
            return "happy"

        for store in stores:
            if (
                get_distance(now, store) <= (20 * 50) and
                store not in visited
            ):
                queue.append(store)
                visited.add(store)

    return "sad"


# t: 테스트 케이스의 수
t = int(read())

answers = []
for _ in range(t):
    # n: 맥주를 파는 편의점의 개수
    n = int(read())

    # home: 상근이네 집 좌표
    home = list(map(int, read().split()))

    # store: 편의점 좌표
    store = set()
    for _ in range(n):
        x, y = map(int, read().split())
        store.add((x, y))

    # festival: 페스티벌 좌표
    festival = list(map(int, read().split()))

    answers.append(can_go(home, store, festival))

for answer in answers:
    print(answer)
