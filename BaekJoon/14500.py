import sys
read = sys.stdin.readline


# r, c : 현재 확인할 위치, count: 지금까지 포함한 칸의 수
# now_sum: 지금까지 포함한 칸에 적힌 수의 합, checked: 지금까지 포함한 칸
def set_max_sum(r, c, count, now_sum, checked):
    # 남은 모든 칸이 최댓값이더라도 이미 구한 값보다 작다면 더이상 확인하지 않는다.
    if now_sum + MAX_VAL * (4 - count) < max_sum[0]:
        return

    if count == 4:  # 4개를 정했으면
        max_sum[0] = max(now_sum, max_sum[0])
        return

    # 상하좌우 네 방향으로 탐색한다.
    for dr, dc in drdc:
        dr, dc = r + dr, c + dc
        if 0 <= dr < N and 0 <= dc < M and (dr, dc) not in checked:
            checked.add((dr, dc))
            # 다음 위치로 이동해서 탐색한다.
            set_max_sum(dr, dc, count + 1, now_sum + board[dr][dc], checked)
            # 두 개의 칸을 정했을 때는 ㅜ, ㅗ, ㅏ, ㅓ 모양을 위해 현재 위치에서 한번 더 탐색해준다.
            if count == 2:
                set_max_sum(r, c, count + 1, now_sum + board[dr][dc], checked)
            checked.remove((dr, dc))


N, M = map(int, read().split())  # N: 행 수, M: 열 수
board = [list(map(int, read().split())) for _ in range(N)]

max_sum = [0]
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
MAX_VAL = max(map(max, board))  # 종이 위의 숫자들 중 최대값

for i in range(N):
    for j in range(M):
        set_max_sum(i, j, 1, board[i][j], set([(i, j)]))

print(*max_sum)
