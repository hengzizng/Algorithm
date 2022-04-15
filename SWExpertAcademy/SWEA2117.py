import sys
sys.stdin = open("TestCase/SWExpertAcademy/2117input.txt")


def get_max_house_count(r, c, k):
    house_count = 0

    for house in houses:
        # (r, c) ~ house 거리가 k 미만이면
        if abs(house[0] - r) + abs(house[1] - c) < k:
            house_count += 1

    # (r, c) 위치에서 k 범위로 서비스를 운영하지 못하면
    if house_count * M < (k ** 2 + (k - 1) ** 2):
        house_count = 0

    if max_house_count < house_count:
        return house_count
    else:
        return max_house_count


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    N, M = map(int, input().split())  # 도시 크기, 하나의 집이 지불가능한 비용
    city = [list(map(int, input().split())) for _ in range(N)]
    houses = [(r, c) for r in range(N) for c in range(N) if city[r][c] == 1]

    max_k = (N + 1) if N % 2 == 0 else N
    max_house_count = 0  # 서비스를 제공 받는 최대 집의 수

    if len(houses) * M >= (max_k ** 2 + (max_k - 1) ** 2):
        print("#%d" % t, len(houses))
        continue

    for k in range(max_k - 1, 1 - 1, -1):  # (max_k-1 ~ 1) 내림차순
        cost = (k ** 2) + ((k - 1) ** 2)
        for r in range(N):
            for c in range(N):
                max_house_count = get_max_house_count(r, c, k)

        if max_house_count > 1:
            break

    print("#%d" % t, max_house_count)
