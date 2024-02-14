from collections import deque
import sys
read = sys.stdin.readline


def drop(r, c, blocks):
    if blocks[r][c] == 0:
        return 0
    
    queue = deque([(r, c)])
    blocks[r][c] = 0
    drop_count = 1

    # 처음 떨어진 블럭 기준으로 탐색
    while queue:
        # 이번에 떨어진 블럭
        r, c = queue.popleft()

        # 이번에 떨어진 블럭에 접한 블럭들 탐색
        for d in range(len(drdc)):
            nr, nc = r + drdc[d][0], c + drdc[d][1]
            if 0 <= nr < n and 0 <= nc < m and blocks[nr][nc] == 1:
                # 이번에 떨어진 블럭에 접한 블럭이므로, 좌우 또는 위아래 중 1개 이상 접한 블럭이 없을 경우 떨어짐
                check_d = d
                for i in range(1, 2 + 1, 1):
                    check_d = (check_d + i) % 4
                    nnr, nnc = nr + drdc[check_d][0], nc + drdc[check_d][1]
                    if 0 <= nnr < n and 0 <= nnc < m and blocks[nnr][nnc] == 0:
                        queue.append((nr, nc))
                        blocks[nr][nc] = 0
                        drop_count += 1
                        break

    return drop_count


drdc = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 북동남서
T = int(read()) # 테스트케이스 수
for _ in range(T):
    # n: 프레임 내 블럭이 채워진 사각형의 가로 크기
    # m: 프레임 내 블럭이 채워진 사각형의 세로 크기
    # q: 움직임 횟수(블럭을 떨어뜨리는 횟수)
    n, m, q = map(int, read().split())
    # 블럭의 현재 상태
    blocks = [[1] * m for _ in range(n)]
    for _ in range(q):
        # 이번에 떨어뜨릴 블럭의 위치
        x, y = map(lambda x: int(x) - 1, read().split())
        print(drop(x, y, blocks))
