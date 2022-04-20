import sys
sys.stdin = open("TestCase/SWExpertAcademy/2382input.txt")


# 각 위치별로 미생물 군집들이 이동
def move():
    global microbes
    moved_microbes = {}

    for r, c in microbes:
        # 이번에 움직일 군집 정보
        count, d, max_count = microbes[(r, c)]

        # 새로 이동할 위치
        nr, nc = r + drdc[d][0], c + drdc[d][1]

        # 약품으로의 이동이라면
        if nr % (N - 1) == 0 or nc % (N - 1) == 0:
            count = count // 2  # 살아남은 미생물 수
            d = d ^ 1  # 방향을 반대로 변경

        # 이동한 위치에 이미 도착한 군집이 있다면
        if (nr, nc) in moved_microbes:
            # 이번에 움직인 군집의 미생물 수가 더 많다면
            if count > moved_microbes[(nr, nc)][2]:
                moved_microbes[(nr, nc)][1] = d
                moved_microbes[(nr, nc)][2] = count
            moved_microbes[(nr, nc)][0] += count
        # 이번 군집이 이동한 위치에 도착한 첫 군집이라면
        else:
            moved_microbes[(nr, nc)] = [count, d, count]

    microbes = moved_microbes


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
T = int(input())  # 테스트케이스 수
for t in range(1, T + 1):
    # N: 한 변 길이, M: 격리 시간, K: 미생물 군집의 수
    N, M, K = map(int, input().split())

    # 모든 미생물 군집 정보 {(행, 열) : [미생물 수, 방향, 이 위치의 군집들 중 가장 많은 미생물 수], ...}
    microbes = {}
    for k in range(K):
        # 행, 열, 미생물 수, 이동 방향
        r, c, count, d = map(int, input().split())
        microbes[(r, c)] = [count, d - 1, count]

    for m in range(M):
        move()

    alive_count = 0
    for microbe_no in microbes:
        alive_count += microbes[microbe_no][0]

    print("#%d" % t, alive_count)
