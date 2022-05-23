from collections import deque
import sys
read = sys.stdin.readline


# start_area 구역과 연결된, 같은 지역구 내 모든 구역의 수 반환
def get_group(start_area, group_type, selected):
    queue = deque([start_area])
    visited = set([start_area])

    while queue:
        now_area = queue.popleft()
        for next_area in graph[now_area]:
            if next_area in visited or selected[next_area] != group_type:
                continue
            visited.add(next_area)
            queue.append(next_area)

    return len(visited)


# target_count 만큼 구역을 선택
def select_group1(target_count, count, start, population, selected):
    if count == target_count:
        if answer[0] < abs(total_population - (2 * population)):
            return
            
        group1_check, group2_check = False, False
        visited_count = 0

        for area, group_type in enumerate(selected):
            # 첫 번째 선거구 확인
            if not group1_check and group_type == 0:
                group1_check = True
                visited_count += get_group(area, group_type, selected)
            # 두 번째 선거구 확인
            if not group2_check and group_type == 1:
                group2_check = True
                visited_count += get_group(area, group_type, selected)

        # 두 선거구를 모두 확인했을 때 모든 지역을 포함한다면
        if visited_count == N:
            answer[0] = min(answer[0], abs(total_population - (2 * population)))

        return

    for i in range(start, N):
        selected[i] = 1
        select_group1(target_count, count + 1, i + 1, population + populations[i], selected)
        selected[i] = 0


N = int(read())  # 구역의 개수
populations = list(map(int, read().split()))  # 각 구역의 인구
total_population = sum(populations)  # 총 인구 수
answer = [total_population]  # 두 선거구의 인구 차이의 최솟값
graph = {}  # 각 구역과 인접한 구역의 정보
for i in range(N):
    graph[i] = list(map(lambda x: int(x) - 1, read().split()))[1:]

# 각 선거구에 포함될 구역의 수를 정한다.
for group1_count in range(1, N // 2 + 1):
    group2_count = N - group1_count
    # 정해진 구역의 수에 따라 구역을 선택한다.
    select_group1(group1_count, 0, 0, 0, [0] * N)

print(-1 if answer[0] == total_population else answer[0])
