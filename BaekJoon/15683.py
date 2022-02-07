import sys
read = sys.stdin.readline


# 각 CCTV별로 방향을 설정햔다
def set_direction(count, moniter_count, office):
    if count == cctv_count:
        max_moniter_count[0] = max(max_moniter_count[0], moniter_count)
        return

    cctv_type = cctv_info[count + 7][0]
    for index in range(len(d_by_cctv[cctv_type])):
        copied = get_copied(office)
        now_moniter_count = set_moniter_area1(count + 7, index, copied)
        set_direction(count + 1, moniter_count + now_moniter_count, copied)


# 이번 CCTV로 감시할 수 있는 부분을 표시하고 그 구역 수를 리턴한다
def set_moniter_area1(cctv_no, cctv_dir, office):
    moniter_count = 0  # 이번 CCTV를 통해 사각지대에서 제외된 영역 수
    cctv_type, r, c = cctv_info[cctv_no]

    # CCTV의 감시 방향별로 반복(2번이면 좌,우 또는 상,하)
    for now_dir in d_by_cctv[cctv_type][cctv_dir]:
        dr, dc = drdc[now_dir]
        nr, nc = r + dr, c + dc
        while 0 <= nr < N and 0 <= nc < M and office[nr][nc] < 6:
            if office[nr][nc] == 0:
                office[nr][nc] = -1
                moniter_count += 1
            nr, nc = nr + dr, nc + dc

    return moniter_count


# 복사한 배열을 리턴한다
def get_copied(arr):
    copied = [[0] * M for _ in range(N)]

    for n in range(N):
        for m in range(M):
            copied[n][m] = arr[n][m]

    return copied


# 방향을 나타낸다 (0: 북, 1: 동, 2: 남, 3: 서)
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 각 CCTV별로 가능한 감시할 수 있는 방향 조합
d_by_cctv = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]

# N: 행 수, M: 열 수
N, M = map(int, read().split())

# cctv_info[7~] : CCTV 번호로 CCTV 정보(종류, 행 위치, 열 위치)를 저장
cctv_count, cctv_info = 7, {}
zero_count = 0
office = []
for n in range(N):
    office.append(list(map(int, read().split())))
    for m in range(M):
        if office[n][m] == 0:
            zero_count += 1
        elif office[n][m] <= 5:
            cctv_info[cctv_count] = (office[n][m], n, m)
            cctv_count += 1
cctv_count -= 7

max_moniter_count = [0]
set_direction(0, 0, office)

print(zero_count - max_moniter_count[0])
