from collections import defaultdict


N, D = map(int, input().split())
shortcut = defaultdict(list)
for _ in range(N):
    start, end, distance = map(int, input().split())

    if end > D:
        continue

    shortcut[end].append((start, distance))


min_distance = [0]
for position in range(1, D + 1):
    min_distance.append(min_distance[position - 1] + 1)

    if position in shortcut:
        for start, distance in shortcut[position]:
            min_distance[position] = min(
                min_distance[position], min_distance[start] + distance)

print(min_distance[D])
