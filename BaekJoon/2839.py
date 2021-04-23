N = int(input())

d = [float('inf')] * 5001
d[3] = 1
d[5] = 1

for i in range(6, N + 1):
    d[i] = min(d[i - 3], d[i - 5]) + 1

print(-1 if d[N] == float('inf') else d[N])