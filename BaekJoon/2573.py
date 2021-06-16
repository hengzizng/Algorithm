from collections import deque
import sys
read = sys.stdin.readline

def solution():
    N, M = map(int, read().split())
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def get_iceberg_start(arctic, start):
        for row in range(start[0], N):
            for col in range(start[1], M):
                if arctic[row][col] > 0:
                    return (row, col)
        return (-1, -1)

    def get_iceberg_part_count(arctic, start):
        queue = deque([start])
        visited = set([start])

        while queue:
            row, col = queue.popleft()

            for x, y in direction:
                x, y = x + row, y + col
                if (
                    0 <= x < N and 0 <= y < M and
                    arctic[x][y] > 0 and
                    (x, y) not in visited
                ):
                    visited.add((x, y))
                    queue.append((x, y))
        
        return len(visited)

    def melting(arctic, start):
        queue = deque([start])
        visited = set([start])
        melt_count = [[0] * M for _ in range(N)]

        while queue:
            row, col = queue.popleft()

            for x, y in direction:
                x, y = x + row, y + col
                if (
                    0 <= x < N and 0 <= y < M and
                    (x, y) not in visited
                ):
                    if arctic[x][y] > 0:
                        visited.add((x, y))
                        queue.append((x, y))
                    else:
                        melt_count[row][col] += 1
        
        total_iceberg_count = 0
        for row in range(N):
            for col in range(M):
                if arctic[row][col] > melt_count[row][col]:
                    arctic[row][col] -= melt_count[row][col]
                    total_iceberg_count += 1
                else:
                    arctic[row][col] = 0
        
        return total_iceberg_count


    # arctic: 현재 북극 상태
    arctic = []
    for _ in range(N):
        arctic.append(list(map(int, read().split())))

    year = 0
    start = get_iceberg_start(arctic, [0, 0])
    part_iceberg_count, total_iceberg_count = 0, 0
    while part_iceberg_count == total_iceberg_count:
        total_iceberg_count = melting(arctic, start)
        start = get_iceberg_start(arctic, start)
        if start == (-1, -1):
            return 0
        part_iceberg_count = get_iceberg_part_count(arctic, start)
        year += 1
    
    return year


print(solution())