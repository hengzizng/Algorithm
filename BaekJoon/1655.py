from heapq import *
import sys
read = sys.stdin.readline


N = int(read())  # 정수의 개수
min_heap, max_heap = [], []  # 최소 힙의 root(최소값) >= 최대 힙의 root(최대값)
for last_idx in range(N):
    num = int(read())  # 추가할 정수

    if len(min_heap) == len(max_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    # 조건에 맞지 않으면 각 root값들을 교환한다.
    if min_heap and min_heap[0] < (max_heap[0] * -1):
        temp1 = heappop(min_heap) * -1
        temp2 = heappop(max_heap) * -1

        heappush(min_heap, temp2)
        heappush(max_heap, temp1)

    print(-1 * max_heap[0])
