from collections import defaultdict
import sys
# sys.stdin = open("TestCase/BaekJoon/17780input.txt")
read = sys.stdin.readline


# 다음 칸이 흰색(0): 그냥 이동
# 다음 칸이 빨간색(1): 이동 후 [현재 말 ~ 가장 위 말] 들을 뒤집음
# 다음 칸이 파란색(2) or 바깥
# - 처음이면 방향 바꿔서 다시 이동 시도
# - 두번째면 방향만 바꾼 채로 멈춤

# 말이 4개 이상 쌓이는 순간 종료 -> 몇 번째 턴인지 출력
# 1001번째 턴 이상이면 -1 출력


# 말 하나가 움직인다. 말이 4개 이상 쌓이면 True를 반환
def move(no, try_count):
    r, c, d = meeples[no]

    # 가장 아래 말이 아니면 움직이지 않음
    if list_by_loc[(r, c)][0] != no:
        return False

    # 이동하려는 위치
    nr, nc = r + drdc[d][0], c + drdc[d][1]

    # 이동하려는 칸이 체스판 밖이거나 파란색인 경우
    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:
        if try_count == 0:
            meeples[no][2] = d ^ 1
            return move(no, 1)
        else:
            return False
    # 이동하려는 칸이 흰색인 경우
    elif board[nr][nc] == 0:
        for move_no in list_by_loc[(r, c)]:
            meeples[move_no][0], meeples[move_no][1] = nr, nc
            list_by_loc[(nr, nc)].append(move_no)
        list_by_loc.pop((r, c))
    # 이동하려는 칸이 빨간색인 경우
    else:
        while list_by_loc[(r, c)]:
            # 움직이려는 말의 번호
            move_no = list_by_loc[(r, c)].pop()
            meeples[move_no][0], meeples[move_no][1] = nr, nc
            list_by_loc[(nr, nc)].append(move_no)

    # 말이 4개 이상 쌓였다면
    if len(list_by_loc[(nr, nc)]) >= 4:
        return True
    else:
        return False



# 각 턴을 플레이한다. 종료되었다면 True를 반환
def play():
    for no in range(K):
        if move(no, 0):
            return True
    return False


# →, ←, ↑, ↓
drdc = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# N: 체스판의 크기, K: 말의 개수
N, K = map(int, read().split())
# 0: 흰색, 1: 빨간색, 2: 파란색
board = [list(map(int, read().split())) for _ in range(N)]
# meeples: 말 정보 [행, 열, 이동 방향], list_by_loc: 위치별 말 리스트 (index 0: 아래)
meeples, list_by_loc = [], defaultdict(list)
for no in range(K):
    # 행, 열, 이동 방향
    r, c, d = map(lambda x: int(x) - 1, read().split())
    meeples.append([r, c, d])
    # 같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다.
    list_by_loc[(r, c)] = [no]

# 1000번 턴까지 게임 플레이
result = -1
for turn in range(1, 1000 + 1):
    if play():
        result = turn
        break
print(result)
