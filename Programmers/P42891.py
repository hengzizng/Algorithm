def solution(food_times, k):
    count_by_time = [0] * 100000001
    for time in food_times:
        count_by_time[time] += 1

    total_time = 0  # 현재 시간
    left_food = len(food_times)  # 남은 음식 개수
    for time in range(1, 100000001):  # 각 음식을 먹는 데 걸리는 시간별 탐색
        # 음식을 다 먹었다면 종료
        if left_food == 0:
            return -1

        # 시간 누적
        total_time += left_food
        # 남은 음식 수 갱신
        left_food -= count_by_time[time]

        if total_time + left_food > k:
            break

    for food_idx in range(len(food_times)):
        food_time = food_times[food_idx]

        if food_time > time:
            total_time += 1

        if total_time == k + 1:
            break

    return food_idx + 1


print(solution([3, 1, 2], 5), "=>", 1)
print(solution([100000000, 1, 2], 5), "=>", 1)
