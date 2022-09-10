import sys
read = sys.stdin.readline


def solution(n, weak, dist):
    # dist 중 공사에 사용될 값을 선택 (is_put: 공사에 투입되었는지 여부)
    def select_friend(count, selected, is_put):
        if answer[0] > -1:
            return

        if target_count == count:
            # 시작점을 변경해가며 점검 가능한지 확인
            for start in range(len(weak)):
                if check(start, selected):
                    answer[0] = count
                    break
            return

        for i in range(len(dist)):
            if not is_put[i]:
                is_put[i] = True
                selected[count] = dist[i]
                select_friend(count + 1, selected, is_put)
                is_put[i] = False

    # 시작점(weak 중 한 지점)에서부터 selected로 점검 가능한지 확인
    def check(start, selected):
        selected_idx = 0  # selected의 인덱스 변수
        dist_sum = 0  # selected[selected_idx]로 점검할 거리의 합
        for i in range(start, start + len(weak) - 1):  # 각 지점 순회
            now_idx = i % len(weak)  # 이번에 점검할 지점의 인덱스
            next_idx = (i + 1) % len(weak)  # 다음에 점검할 지점의 인덱스
            # 이번에 점검할 지점과 다음에 점검할 지점 사이 거리
            now_dist = weak[next_idx] - weak[now_idx]
            if now_idx > next_idx:
                now_dist = (weak[next_idx] + n) - weak[now_idx]

            # 현재 점검중인 친구가 다음 지점까지 점검할 수 없다면
            dist_sum += now_dist
            if dist_sum > selected[selected_idx]:
                selected_idx += 1
                dist_sum = 0

            if selected_idx == len(selected):
                return False

        return True

    answer = [-1]
    for target_count in range(1, len(dist) + 1):
        if answer[0] == -1:
            select_friend(0, [-1] * target_count, [False] * len(dist))
        else:
            break

    return answer[0]


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), ":", 2)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]), ":", 1)
