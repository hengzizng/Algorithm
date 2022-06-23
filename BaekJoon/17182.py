import sys
read = sys.stdin.readline


def visit(now_planet, time, visit_bit):
    if time > min_time[0]:
        return

    if visit_bit == (1 << N) - 1:
        min_time[0] = time
        return

    for next_planet in range(N):
        if visit_bit & (1 << next_planet) == 0:
            new_visit_bit = visit_bit | (1 << next_planet)
            visit(next_planet, time + times[now_planet][next_planet], new_visit_bit)


N, K = map(int, read().split())
times = [list(map(int, read().split())) for _ in range(N)]
min_times = [[1000] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if times[i][j] > times[i][k] + times[k][j]:
                times[i][j] = times[i][k] + times[k][j]

visit_bit = 1 << K
min_time = [1000 * N]

visit(K, 0, visit_bit)

print(min_time[0])
