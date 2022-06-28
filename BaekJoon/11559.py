from collections import deque
import sys
read = sys.stdin.readline


def drop():
    for c in range(W):
        # 뿌요들을 아래로 떨어뜨린다.
        new_r = H - 1
        for r in range(H - 1, 0 - 1, -1):
            if board[r][c] != '.':
                board[new_r][c] = board[r][c]
                new_r -= 1
        # 윗부분을 빈 칸으로 만들어준다.
        for r in range(new_r, 0 - 1, -1):
            board[r][c] = '.'


# 터졌으면 1, 터지지 않았으면 0 반환
def explode(visit, r, c):
    color = board[r][c]  # 터질 색상
    targets = []  # 터질 위치
    queue = deque([(r, c)])

    while queue:
        now = queue.popleft()

        for nr, nc in drdc:
            nr, nc = now[0] + nr, now[1] + nc
            if 0 <= nr < H and 0 <= nc < W and not visit[nr][nc] and board[nr][nc] == color:
                queue.append((nr, nc))
                targets.append((nr, nc))
                visit[nr][nc] = True

    # 4개 이하이면 터지지 않는다.
    if len(targets) < 4:
        return 0
    
    # 터진 곳을 빈 칸으로 만든다.
    for r, c in targets:
        board[r][c] = '.'
    return 1


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 필드의 세로, 가로 길이
H, W = 12, 6
# 필드 상태
board = [list(read().strip()) for _ in range(H)]
# 연쇄 횟수
explode_count = 0

# 터지지 않을 때까지 반복
while True:
    # 이번 한번에 터진 횟수
    now_explode_count = 0
    # 방문 여부
    visit = [[False] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if not visit[r][c] and board[r][c] != '.':
                now_explode_count += explode(visit, r, c)

    if now_explode_count == 0:
        break

    explode_count += 1
    drop()

print(explode_count)