from collections import deque
import sys
read = sys.stdin.readline


# 온풍기에서 바람이 한 번 출력
def heat(r, c, d, room):
    queue = deque([(r, c, 5)])
    checked = set()
    flag = 0  # 0일 때는 d 방향으로 퍼지고, 1일 때는 d의 수직 방향으로 퍼진다.
    while queue:
        for _ in range(len(queue)):
            r, c, temperature = queue.popleft()

            if flag == 0:  # d방향
                nr, nc = r + drdc[d][0], c + drdc[d][1]
                if not is_valid(r, c, nr, nc) or (nr, nc) in checked:
                    continue
                room[nr][nc] += temperature
                if temperature > 1:
                    queue.append((nr, nc, temperature - 1))
                    checked.add((nr, nc))
            else:  # d의 수직 방향 (방향 0 / 1 이라면 -> 2, 3    방향 2 / 3 이라면 -> 0, 1)
                queue.append((r, c, temperature))
                checked.add((r, c))

                nd = 0 if d // 2 == 1 else 2
                for i in range(2):
                    nr, nc = r + drdc[nd + i][0], c + drdc[nd + i][1]
                    if not is_valid(r, c, nr, nc) or (nr, nc) in checked:
                        continue
                    queue.append((nr, nc, temperature))
                    checked.add((nr, nc))

        flag = (flag + 1) % 2


# 온도 조절
def adjust(room):
    # 복사 배열을 만든다
    adjusted = []
    for r in range(R):
        adjusted.append([])
        for c in range(C):
            adjusted[r].append(room[r][c])

    for r in range(R):
        for c in range(C):
            for i in range(2):
                nd = (3 + i) % 4  # 우, 하 를 확인하기 위해 사용
                nr, nc = r + drdc[nd][0], c + drdc[nd][1]
                # 두 칸의 온도차가 4 이상일때만 체크
                if is_valid(r, c, nr, nc) and abs(room[r][c] - room[nr][nc]) >= 4:
                    val = abs(room[r][c] - room[nr][nc]) // 4
                    if room[r][c] > room[nr][nc]:  # 확인중인 칸이 더 크면
                        adjusted[r][c] -= val
                        adjusted[nr][nc] += val
                    else:  # 확인중인 칸이 더 작으면
                        adjusted[r][c] += val
                        adjusted[nr][nc] -= val

    return adjusted


# 가장 바깥쪽 칸의 온도가 1씩 감소
def decrease(room):
    for c in range(C):  # 0, R-1 행의 모든 열에 대해 감소
        room[0][c] = max(room[0][c] - 1, 0)
        room[R - 1][c] = max(room[R - 1][c] - 1, 0)
    for r in range(1, R - 1):  # 0, C-1 열의 1 ~ R-2 행에 대해 감소
        room[r][0] = max(room[r][0] - 1, 0)
        room[r][C - 1] = max(room[r][C - 1] - 1, 0)


# 조사하는 모든 칸의 온도가 K 이상인지 확인
def check():
    for r, c in check_list:
        if room[r][c] < K:
            return False
    return True


# 유효성 검사
def is_valid(r, c, nr, nc):
    if 0 <= nr < R and 0 <= nc < C and (r, c, nr, nc) not in walls:
        return True
    else:
        return False


drdc = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # 우, 좌, 상, 하
R, C, K = map(int, read().split())  # R: 행 수, C: 열 수, K(이상): 기준 온도

# room: 방 정보, check_list: 온도를 조사할 칸, heaters: 온풍기 정보
room, check_list, heaters = [], [], []
for r in range(R):
    room.append(list(map(int, read().split())))
    for c in range(C):
        val = room[r][c]
        if val == 0:
            continue
        if val == 5:  # 온도를 조사해야하는 칸
            check_list.append((r, c))
        else:  # 온풍기
            heaters.append((r, c, val - 1))
        room[r][c] = 0


W = int(read())  # 벽의 개수
walls = set()  # 벽 정보
for w in range(W):
    x, y, t = map(int, read().split())
    x, y = x - 1, y - 1
    if t == 0:
        nx, ny = x - 1, y
    else:
        nx, ny = x, y + 1
    walls.add((x, y, nx, ny))
    walls.add((nx, ny, x, y))


chocolate = 0
for chocolate in range(1, 101 + 1):
    for r, c, d in heaters:  # 온풍기별로 반복: 행, 열, 방향(0~3, 우좌상하)
        heat(r, c, d, room)  # 각 온풍기마다 바람이 나온다

    room = adjust(room)  # 온도 조절
    decrease(room)  # 가장 바깥쪽 칸의 온도가 1씩 감소

    if check():
        break

print(chocolate)
