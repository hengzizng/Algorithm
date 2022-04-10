import sys
sys.stdin = open("TestCase/SWExpertAcademy/2105input.txt")


def get_dessert_count(move_count, r, c):
    # 다음에 확인할 위치
    nr, nc = r, c
    # 움직일 방향에 따른 인덱스, 이번 변에서 남은 이동 횟수
    move_flag, left_move_count = 0, move_count[0]
    # 디저트 종류 집합
    dessert_kind = set()

    while True:
        # 이번 위치의 디저트를 이미 먹은 적 있으면
        if cafes[nr][nc] in dessert_kind:
            return -1

        dessert_kind.add(cafes[nr][nc])

        # 이번 변에서 남은 이동 횟수가 없다면 방향을 바꿔야 한다.
        if left_move_count == 0:
            move_flag = (move_flag + 1) % 4
            left_move_count = move_count[move_flag % 2]

        left_move_count -= 1
        nr, nc = nr + drdc[move_flag][0], nc + drdc[move_flag][1]

        # 다시 출발지로 돌아왔다면 종료
        if nr == r and nc == c:
            return len(dessert_kind)


def set_condition():
    # 한 변에서의 이동 횟수를 정한다.
    for i in range(1, N - 1):  # 오른쪽 위, 왼쪽 아래
        for j in range(1, N - i):  # 오른쪽 아래, 왼쪽 위
            # 시작 위치를 정한다.
            for r in range(0, N - (i + j)):  # 시작 지점의 행
                for c in range(j, N - i):  # 시작 지점의 열
                    now_count = get_dessert_count([i, j], r, c)
                    max_dessert_count[0] = max(max_dessert_count[0], now_count)


drdc = [[1, 1], [1, -1], [-1, -1], [-1, 1]]  # 북 -> 동 -> 남 -> 서
T = int(input())  # 테스트케이스 수
for t in range(1, T + 1):
    # 지역의 한 변의 길이
    N = int(input())
    # 카페에서 팔고 있는 디저트 정보
    cafes = [list(map(int, input().split())) for _ in range(N)]

    # 최대 디저트 수
    max_dessert_count = [-1]
    # 조건을 정하고, 최대 디저트 수를 구해 갱신한다.
    set_condition()

    print("#", end="")
    print(t, max_dessert_count[0])
