import sys
read = sys.stdin.readline


# 팀을 구한다 (team - True: 스타트 팀, False: 링크 팀)
# s_count / l_count: 스타트 / 링크 팀의 인원 수
# s_val / l_val: 스타트 / 링크 팀의 능력치 합
def set_team(s_count, l_count, s_val, l_val, team):
    total_count = s_count + l_count

    if total_count == N:
        min_diff[0] = min(min_diff[0], abs(s_val - l_val))
        return

    # 이번에 선택한 사람에 대한 능력치를 더한다
    now_s_val, now_l_val = 0, 0
    for before in range(total_count):
        # 이번에 선택한 사람과 확인할 사람의 능력치 합
        temp = S[before][total_count] + S[total_count][before]
        if team[before]:  # 스타트 팀
            now_s_val += temp
        else:  # 링크 팀
            now_l_val += temp

    # 이번에 선택한 사람은 스타트 팀
    if s_count < (N // 2):
        team[total_count] = True
        set_team(s_count + 1, l_count, s_val + now_s_val, l_val, team)
    # 이번에 선택한 사람은 링크 팀
    if l_count < (N // 2):
        team[total_count] = False
        set_team(s_count, l_count + 1, s_val, l_val + now_l_val, team)


N = int(read())
S = [list(map(int, read().split())) for _ in range(N)]
min_diff = [100 * N * N]
set_team(0, 0, 0, 0, [False] * N)

print(*min_diff)
