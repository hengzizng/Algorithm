import sys
read = sys.stdin.readline


# 스타트 팀을 구한다 (나머지는 자동 링크 팀)
def get_start_team(start, count, start_team):
    if count == N // 2:
        j = 0
        link_team = []
        for i in range(N):
            if j < (N // 2) and i == start_team[j]:
                j += 1
            else:
                link_team.append(i)

        start_team_sum, link_team_sum = 0, 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                start_team_sum += S[start_team[i]][start_team[j]]
                start_team_sum += S[start_team[j]][start_team[i]]
                link_team_sum += S[link_team[i]][link_team[j]]
                link_team_sum += S[link_team[j]][link_team[i]]

        min_diff[0] = min(min_diff[0], abs(start_team_sum - link_team_sum))

        return

    for index in range(start, N):
        start_team[count] = index
        get_start_team(index + 1, count + 1, start_team)


N = int(read())
S = [list(map(int, read().split())) for _ in range(N)]
min_diff = [100 * N * N]
get_start_team(0, 0, [-1] * (N // 2))

print(*min_diff)
