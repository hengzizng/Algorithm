from collections import deque
import sys
read = sys.stdin.readline


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
W, H = map(int, read().split())  # 너비, 높이
board = [list(read().strip()) for _ in range(H)]  # 지도
visited = [[W * H] * W for _ in range(H)]  # 각 칸에 도착하려면 필요한 거울의 최솟값

# 'C' 로 표시되어 있는 칸을 찾는다.
depart, dest = [-1, -1], [-1, -1]
for r in range(H):
    for c in range(W):
        if board[r][c] == 'C':
            if depart[0] == -1:
                depart = [r, c]
            else:
                dest = [r, c]


queue = deque([(depart[0], depart[1])])  # bfs를 위한 큐 (행, 열)
visited[depart[0]][depart[1]] = 0

while queue:
    r, c = queue.popleft()

    for nd in range(4):
        nr, nc = r + drdc[nd][0], c + drdc[nd][1]

        # 거울을 더 추가하지 않고 이동할 수 있는 만큼 이동
        while 0 <= nr < H and 0 <= nc < W and board[nr][nc] != '*':
            # 가려는 위치에 더 적은 거울로도 이동 가능하다면
            if visited[r][c] + 1 > visited[nr][nc]:
                break

            queue.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

            nr += drdc[nd][0]
            nc += drdc[nd][1]

# 'C'에서는 어떤 방향으로도 이동할 수 있기 때문에 처음에 더한 1 값을 빼준다
print(visited[dest[0]][dest[1]] - 1)
