# 70 min

import sys
sys.stdin = open("TestCase/SWExpertAcademy/1949input.txt")


def set_max_len(row, col, height, distance, is_cut, visited):
    max_len[0] = max(max_len[0], distance)

    for nr, nc in drdc:  # 인접한 네 방향 탐색
        nr, nc = nr + row, nc + col
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
            continue

        # 현재 위치를 깎을 필요가 없다면
        if area[nr][nc] < height:
            visited[nr][nc] = True
            set_max_len(nr, nc, area[nr][nc], distance + 1, is_cut, visited)
            visited[nr][nc] = False
        # if X, elif O (height - 1 이기 때문에)
        # 지금까지 깎은 적 없고 현재 위치를 깎아서 갈 수 있다면
        elif is_cut == 0 and area[nr][nc] - K < height:
            visited[nr][nc] = True
            set_max_len(nr, nc, height - 1, distance + 1, is_cut + 1, visited)
            visited[nr][nc] = False


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 테스트케이스 수
T = int(input())
for t in range(1, T + 1):
    # N: 지도의 한 변의 길이, K: 최대 공사 가능 깊이, area: 지도 정보
    N, K = map(int, input().split())
    area = []
    # max_height: 가장 높은 봉우리의 높이, max_height_info: 가장 높은 봉우리들 정보
    max_height, max_height_info = 0, []
    for r in range(N):
        area.append(list(map(int, input().split())))
        for c in range(N):
            if area[r][c] < max_height:
                continue
            elif area[r][c] > max_height:
                max_height_info.clear()
                max_height = area[r][c]
            # 행, 열, 높이, 거리, 깎은적 있는지 여부(0: 없음, 1이상: 있음)
            max_height_info.append((r, c, max_height, 1, 0))

    max_len = [0]
    for top in max_height_info:
        visited = [[False] * N for _ in range(N)]
        visited[top[0]][top[1]] = True  # 현재 위치 방문체크
        set_max_len(*top, visited)
    print("#%d" % t, max_len[0])
