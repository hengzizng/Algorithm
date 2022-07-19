from collections import deque
import sys
read = sys.stdin.readline


# n: 트럭 수, w: 다리 길이, L: 다리 최대 하중
n, w, L = map(int, read().split())
# 트럭들의 무게
trucks = list(map(int, read().split()))

# 다리 위에 있는 트럭 정보 [(다리를 건너기 시작한 시간, 무게), ...]
bridge = deque()
# 다리 위에 있는 트럭의 무게 합, 현재 시각
weight_sum, time = 0, 1
# 모든 트럭별로 반복
for truck in trucks:
    # 다리를 다 건넌 트럭들을 제거
    while bridge and bridge[0][0] + w <= time:
        on_time, weight = bridge.popleft()
        weight_sum -= weight

    # 이번 트럭이 다리에 진입할 수 있는 조건을 만든다
    while len(bridge) == w or weight_sum + truck > L:
        on_time, weight = bridge.popleft()
        weight_sum -= weight
        time = on_time + w

    # 이번 트럭 다리에 진입
    bridge.append((time, truck))
    weight_sum += truck

    time += 1

# 마지막으로 다리를 건너기 시작한 트럭이 다리를 다 건너는 시간 출력
print(bridge[-1][0] + w)
