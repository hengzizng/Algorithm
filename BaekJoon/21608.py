import sys
read = sys.stdin.readline


# 현재 칸에 인접한 좋아하는 학생의 수를 구한다
def get_like_and_blank_count(student, position, like_list):
    like_count, blank_count = 0, 0

    for dr, dc in drdc:
        dr, dc = dr + position[0], dc + position[1]
        if 0 <= dr < N and 0 <= dc < N:
            if classroom[dr][dc] in like_list[student]:
                like_count += 1
            elif classroom[dr][dc] == 0:
                blank_count += 1

    return like_count, blank_count


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# N: 교실 크기
N = int(read())

order = []
like_list = {}
for _ in range(N * N):
    info = list(map(int, read().split()))
    order.append(info[0])
    like_list[info[0]] = set(info[1:])

classroom = [[0] * N for _ in range(N)]  # 교실 정보
for student in order:  # 학생별로 순서대로 반복
    info = [0, 0, -1, -1]  # 현재 학생에 대한 정보 [인접한 좋아하는 학생의 수, 인접한 빈 칸 수, 행, 열]
    for r in range(N - 1, 0 - 1, -1):  # 가장 아래부터 확인
        for c in range(N - 1, 0 - 1, -1):  # 가장 오른쪽부터 확인
            if classroom[r][c] == 0:  # 비어있는 자리라면
                # 현재 위치에서 인접한 좋아하는 학생의 수와 빈 칸 수를 구한다
                like_count, blank_count = get_like_and_blank_count(
                    student, [r, c], like_list)

                if like_count > info[0]:  # 지금 위치에서 인접한 좋아하는 학생의 수가 이전에 구한 수보다 더 많다면
                    info[0], info[1] = like_count, blank_count
                    info[2], info[3] = r, c
                # 지금 위치에서 인접한 좋아하는 학생의 수가 이전에 구한 수와 같다면
                elif like_count == info[0]:
                    # 지금 위치에서 인접한 빈 칸 수가 이전에 구한 수보다 같거나 많다면
                    if blank_count >= info[1]:
                        info[0], info[1] = like_count, blank_count
                        info[2], info[3] = r, c

    classroom[info[2]][info[3]] = student

# 만족도를 구한다
score = 0
for r in range(N):
    for c in range(N):
        like_count, blank_count = get_like_and_blank_count(
            classroom[r][c], [r, c], like_list)
        if like_count == 1:
            score += 1
        elif like_count == 2:
            score += 10
        elif like_count == 3:
            score += 100
        elif like_count == 4:
            score += 1000

print(score)
