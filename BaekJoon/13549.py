from heapq import *
import sys
read = sys.stdin.readline


def get_min_time():
    pq = [(0, N)]
    min_times = [100001] * 100002
    min_times[N] = 0

    while pq:
        time, loc = heappop(pq)

        if loc == K:
            return time

        if loc - 1 >= 0 and time + 1 < min_times[loc - 1]:
            heappush(pq, (time + 1, loc - 1))
            min_times[loc - 1] = time + 1
        if loc + 1 <= 100000 and time + 1 < min_times[loc + 1]:
            heappush(pq, (time + 1, loc + 1))
            min_times[loc + 1] = time + 1
        if loc * 2 <= 100000 and time < min_times[loc * 2]:
            heappush(pq, (time, loc * 2))
            min_times[loc * 2] = time


# N: 수빈, K: 동생
N, K = map(int, read().split())

# 동생이 수빈이보다 앞에 있다면 순간이동 불가(무조건 걷기만)
if K <= N:
    print(N - K)
else:
    print(get_min_time())
