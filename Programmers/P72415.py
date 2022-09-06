from collections import deque


def solution(board, r, c):
    # 카드 방문 순서를 정한다. (같은 카드는 무조건 연속해서 방문) => 최대 8*7*6*5*4*3*2*1 * 2^8 번
    def set_order(count, distance_sum, before, visited):
        # 이미 구한 최소 조작 수와 같거나 크다면
        if min_move[0] <= distance_sum:
            return

        # 모든 카드를 다 방문했다면
        if count == pair_count * 2:
            min_move[0] = distance_sum
            return

        # 카드쌍별로 방문
        for no in range(1, pair_count + 1):
            # 아직 방문하지 않은 카드쌍일 경우에만 방문
            if visited[no]:
                continue

            # 이번에 방문할 카드쌍의 위치
            r1, c1 = cards_loc[no]
            r2, c2 = cards_loc[no + MAX_PAIR]

            # 이번에 방문한 두 개의 카드 enter 명령어를 포함한 이동 거리(조작 횟수)를 구한다.
            # 앞번호부터 방문
            distance1 = get_distance(*cards_loc[before], r1, c1) + 1
            distance1 += get_distance(r1, c1, r2, c2) + 1
            # 뒷번호부터 방문
            distance2 = get_distance(*cards_loc[before], r2, c2) + 1
            distance2 += get_distance(r2, c2, r1, c1) + 1

            # 방문 처리 (거리를 구한 뒤에 방문처리 해주어야 함!)
            visited[no] = True
            board[r1][c1] = 0
            board[r2][c2] = 0

            # 다음으로 다른 카드 방문
            set_order(count + 2, distance_sum + distance1, no + MAX_PAIR, visited)
            set_order(count + 2, distance_sum + distance2, no, visited)

            # 방문 해제 처리
            visited[no] = False
            board[r1][c1] = no
            board[r2][c2] = no + MAX_PAIR

    # 위치가 board 내에서 유효한지 여부 반환
    def is_valid(row, col):
        if 0 <= row < SIZE and 0 <= col < SIZE:
            return True
        return False

    # 두 위치 간 최단 거리(최소 조작 횟수)를 구한다.
    def get_distance(r1, c1, r2, c2):
        queue = deque([(r1, c1, 0)])
        visited = set([(r1, c1)])

        while queue:
            row, col, distance = queue.popleft()

            # 다른 위치에 도착한 경우 종료
            if row == r2 and col == c2:
                return distance

            # 네 방향으로 이동
            for dr, dc in drdc:
                # 방향키로 이동 (한 칸 이동)
                nr, nc = dr + row, dc + col
                if is_valid(nr, nc):
                    if (nr, nc) not in visited:
                        queue.append((nr, nc, distance + 1))
                        visited.add((nr, nc))
                # 한 칸도 이동할 수 없는 경우는 Ctrl + 방향키로도 이동할 수 없음
                else:
                    continue

                # Ctrl + 방향키 로 이동
                while board[nr][nc] == 0:
                    nr += dr
                    nc += dc
                    # 해당 방향에 카드가 하나도 없을 경우
                    if not is_valid(nr, nc):
                        nr -= dr
                        nc -= dc
                        break
                if (nr, nc) not in visited:
                    queue.append((nr, nc, distance + 1))
                    visited.add((nr, nc))

        # never used
        return abs(r1 - r2) + abs(c1 - c2)

    SIZE = 4  # board의 한 변의 길이
    MAX_PAIR = 8  # 최대 카드쌍 개수
    pair_count = 0  # 카드쌍 개수
    cards_loc = {}  # 각 카드의 위치 (n, n + 8 이 한 쌍의 카드)
    drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

    # board 탐색
    for row in range(SIZE):
        for col in range(SIZE):
            no = board[row][col]

            # 빈 칸일 경우
            if no == 0:
                continue

            # 카드일 경우 위치 저장
            if no in cards_loc:
                cards_loc[no + MAX_PAIR] = (row, col)
                board[row][col] += MAX_PAIR
            else:
                pair_count += 1
                cards_loc[no] = (row, col)

    # 시작 위치 설정
    start_no = board[r][c]
    if board[r][c] == 0:
        cards_loc[17] = (r, c)
        start_no = 17

    # 모든 카드를 제거하기 위한 최소 조작 횟수
    min_move = [float('inf')]
    # 카드 방문 순서를 정하고 순서에 따른 조작 횟수를 구한다. ((r, c)에서 시작)
    set_order(0, 0, start_no, [False] * (MAX_PAIR * 2 + 1))

    return min_move[0]


print(
    solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0),
    14
)
print(
    solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1),
    16
)
