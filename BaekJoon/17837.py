from collections import defaultdict
import sys
read = sys.stdin.readline


def move_one(no, is_blue):
    r, c, d = meeples[no]
    nr, nc = r + dr[d], c + dc[d]

    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:  # 파란색
        if not is_blue:  # 반대로 바꿔서 다시 확인
            # 방향 전환 (2진수에서 1의자리수만 변경해주면 됨)
            # [0] 0 -> [1] 1
            # [1] 1 -> [0] 0
            # [2] 10 -> [3] 11
            # [3] 11 -> [2] 10
            meeples[no][2] = d ^ 1  # 방향 반대로 전환
            return move_one(no, True)
    else:  # 빨간색, 흰색
        index = meeples_by_pos[(r, c)].index(no)  # 이동할 말(no)의 인덱스

        # 이동할 말(no)부터 가장 위까지 모든 말들을 현재 위치에서 없애준다.
        move_meeples = meeples_by_pos[(r, c)][index:]
        meeples_by_pos[(r, c)] = meeples_by_pos[(r, c)][:index]

        if board[nr][nc] == 1:  # 빨간색이면 순서를 반대로 바꾼다
            move_meeples.reverse()

        # 새로운 위치로 이동
        for now in move_meeples:
            meeples[now][0] = nr
            meeples[now][1] = nc
            meeples_by_pos[(nr, nc)].append(now)

    if len(meeples_by_pos[(nr, nc)]) >= 4:
        return True  # 게임 종료

    return False


def move():
    for turn in range(1, 1001 + 1):
        for no in range(K):
            if move_one(no, False):
                return turn
    return -1


# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# N: 체스판 크기, K: 말의 개수
N, K = map(int, read().split())

# 체스판 정보 (0: 흰색, 1: 빨간색, 2: 파란색)
board = [list(map(int, read().split())) for _ in range(N)]
# 말 정보 {말 번호 : [행, 열, 방향]}
meeples = {}
# 체스판 위의 말 정보 {(행, 열) : [아래 말 번호, .. , 위 말 번호]}
meeples_by_pos = defaultdict(list)
for k in range(K):
    r, c, d = map(lambda x: int(x) - 1, read().split())
    meeples[k] = [r, c, d]
    meeples_by_pos[(r, c)].append(k)

print(move())
