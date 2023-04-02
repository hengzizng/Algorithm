import sys
read = sys.stdin.readline


# 체크포인트 수
N = int(read())
# 체크포인트 x, y좌표 리스트
checkpoints = [list(map(int, read().split()))]
# 체크포인트를 모두 방문했을 때의 거리
total_distance = 0
# distances[i]: i번째 체크포인트와 i+1번째 체크포인트 사이의 거리
distances = []
for i in range(N - 1):
    x, y = map(int, read().split())
    distance = abs(x - checkpoints[i][0]) + abs(y - checkpoints[i][1])

    total_distance += distance
    distances.append(distance)

    checkpoints.append([x, y])

min_distance = total_distance
# i: 건너뛸 체크포인트
for i in range(1, N - 1):
    # i-1번째 체크포인트와 i+1번째 체크포인트 사이의 거리
    distance = abs(checkpoints[i - 1][0] - checkpoints[i + 1][0]) + \
        abs(checkpoints[i - 1][1] - checkpoints[i + 1][1])
    min_distance = min(min_distance,
                       total_distance - distances[i - 1] - distances[i] + distance)

print(min_distance)
