from collections import deque


def solution(board):
    # 보드 한 변의 길이
    N = len(board)
    # 방향 벡터 (하우상좌)
    drdc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # (행1, 열1, 로봇이 놓인 방향, 이동 횟수)
    # 방향 - 0: 세로, 1: 가로
    # 위치값(행1, 열1)은 행이나 열이 더 작은 값을 갖는다.
    queue = deque([(0, 0, 1, 0)])
    # (행1, 열1, 로봇이 놓인 방향)
    visited = set([(0, 0, 1)])

    while queue:
        r1, c1, robot_d, mv = queue.popleft()
        r2, c2 = r1 + drdc[robot_d][0], c1 + drdc[robot_d][1]

        # 목적지 도착
        if r2 == N - 1 and c2 == N - 1:
            return mv

        for d in range(4):
            nr1, nc1 = r1 + drdc[d][0], c1 + drdc[d][1]
            nr2, nc2 = r2 + drdc[d][0], c2 + drdc[d][1]

            if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                if (nr1, nc1, robot_d) in visited or board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                    continue

                # 현재 모양을 유지한채로 상하좌우로 이동
                queue.append((nr1, nc1, robot_d, mv + 1))
                visited.add((nr1, nc1, robot_d))

                # 회전
                rotated_d = robot_d ^ 1
                # 로봇 세로 + 오른쪽으로 회전, 로봇 가로 + 아래쪽으로 회전
                if robot_d + d == 1:
                    if (r1, c1, rotated_d) not in visited:
                        queue.append((r1, c1, rotated_d, mv + 1))
                        visited.add((r1, c1, rotated_d))
                    if (r2, c2, rotated_d) not in visited:
                        queue.append((r2, c2, rotated_d, mv + 1))
                        visited.add((r2, c2, rotated_d))
                # 로봇 세로 + 왼쪽으로 회전, 로봇 가로 + 위쪽으로 회전
                elif robot_d + d == 3:
                    if (nr1, nc1, rotated_d) not in visited:
                        queue.append((nr1, nc1, rotated_d, mv + 1))
                        visited.add((nr1, nc1, rotated_d))
                    if (nr2, nc2, rotated_d) not in visited:
                        queue.append((nr2, nc2, rotated_d, mv + 1))
                        visited.add((nr2, nc2, rotated_d))

    return -1
