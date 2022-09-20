from collections import defaultdict


def solution(food_times, k):
    # 음식 섭취시간 오름차순 정렬
    sorted_times = set()
    # 섭취시간별 음식 개수
    count_by_time = defaultdict(int)

    # 섭취시간별 음식 개수를 구한다
    for food_time in food_times:
        sorted_times.add(food_time)
        count_by_time[food_time] += 1
    sorted_times = [0] + sorted(list(sorted_times))

    # 남은 음식 수
    left_food = len(food_times)
    # 누적 시간 (실제 시간)
    time_sum = 0
    # 다 먹은 음식들의 먹는데 걸린 시간들 중 최댓값
    eat_time = 0
    for i in range(1, len(sorted_times)):
        food_time = sorted_times[i]

        # 모든 남아있는 음식을 (sorted_times[i] - sorted_times[i - 1]) 시간만큼 섭취하는 데 걸리는 시간
        now_time = (food_time - sorted_times[i - 1]) * left_food
        if time_sum + now_time > k:
            break

        # 모든 음식을 각각 sorted_time[i] 시간만큼 섭취했을 때 누적 시간 갱신
        time_sum += now_time
        # 음식을 각각 food_time 시간만큼 섭취한 뒤 남은 음식 수 갱신
        left_food -= count_by_time[food_time]
        # 음식을 먹는 데 food_time 이하 걸리는 음식들은 다먹음
        eat_time = food_time

    # 남은 음식이 없다면
    answer = -1
    if left_food == 0:
        return answer

    # 목표 음식까지 남은 시간
    target = (k - time_sum) % left_food
    for food, food_time in enumerate(food_times, 1):
        # 남은 음식만 체크
        if food_time > eat_time:
            if target == 0:
                answer = food
                break
            target -= 1

    return answer


print(solution([3, 1, 2], 5), "=>", 1)
print(solution([100000000, 1, 2], 5), "=>", 1)
print(solution([100000000, 1, 2], 7), "=>", 1)
print(solution([1, 3, 2, 2], 5), "=>", 3)
