from collections import deque
import sys
read = sys.stdin.readline


orders = []
TC = int(read())
for _ in range(TC):
    # N: 문서의 수, M: target 문서의 인덱스
    N, M = map(int, read().split())
    importances = list(map(int, read().split()))

    queue = deque()
    for index, importance in enumerate(importances):
        queue.append((importance, index))

    order = 0
    while queue:
        max_importance, max_index = max(queue)
        importance, index = queue.popleft()

        if max_importance != importance:
            queue.append((importance, index))
            continue

        order += 1
        if index == M:
            break

    orders.append(order)

for order in orders:
    print(order)
