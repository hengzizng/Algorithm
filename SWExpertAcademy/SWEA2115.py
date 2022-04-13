# 90 min

import sys
sys.stdin = open("TestCase/SWExpertAcademy/2115input.txt")
# 행별로 확인
# 열 0 ~ M-1의 수익을 구한다.
# 투포인터로 왼쪽 값 빼고, 오른쪽 값 더하면서 (수익, 행, 시작 열) 값을 profits(배열)에 넣음

# 각 배열(M개의 원소)에서 C보다 같거나 작은 가장 큰 수익을 어떻게 찾을지?
# -> 조합의 합
# 각 합들 중 겹치지 않는 2개의 최대 수익을 어떻게 찾을지?
# -> 2중 for문


# 각 합들 중 겹치지 않는 2개의 최대 수익을 찾는다.
def get_max_profit():
    max_profit = 0

    # profits: [(수익1, 행1, 시작 열1), ...]
    for i in range(len(profits)):
        for j in range(i + 1, len(profits)):
            if profits[i][1] != profits[j][1] or profits[i][2] + M - 1 < profits[j][2]:
                max_profit = max(max_profit, profits[i][0] + profits[j][0])

    return max_profit


# 각 배열(M개의 원소)에서 C보다 같거나 작은 가장 큰 수익 정보를 찾는다.
def get_profit(count, col, amount, profit):
    if count == target_count:
        if amount <= C and profit > honeys_profit[0]:
            honeys_profit[0] = profit
        return

    for now_col in range(col, col_end + 1):
        temp = honeys[row][now_col]
        get_profit(count + 1, now_col + 1, amount + temp, profit + (temp ** 2))


T = int(input())  # 테스트케이스 수
for t in range(1, T + 1):
    # N: 벌통들의 크기, M: 선택할 수 있는 벌통의 개수, C: 꿀을 채취할 수 있는 최대 양
    N, M, C = map(int, input().split())
    # 벌통에서 채취할 수 있는 꿀의 양에 대한 정보
    honeys = [list(map(int, input().split())) for _ in range(N)]
    # 각 시작 위치별로 (수익, 행, 시작 열) 을 담는다.
    profits = []
    for row in range(N):  # 각 부분 배열의 행
        for col_end in range(M - 1, N):  # 각 부분 배열의 마지막 열 인덱스
            for target_count in range(1, M + 1):  # 채취할 꿀의 개수
                honeys_profit = [0]  # 이번 부분 배열의 가능한 가장 큰 수익
                get_profit(0, col_end - M + 1, 0, 0)
                profits.append((honeys_profit[0], row, col_end - M + 1))

    print("#%d" % t, get_max_profit())


'''
# 효율성 좋은 참고 답안
def cal(temp):
    ret = 0
    for i in range(1, (1 << M)):
        tsum = 0
        ttsum = 0
        for j in range(0, M):
            if i & (1 << j):
                tsum += temp[j]
                ttsum += temp[j]**2
        if tsum <= C and ret < ttsum:
            ret = ttsum

    return ret


for tc in range(1, int(input()) + 1):
    N, M, C = list(map(int, input().split()))
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    matt = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            matt[i][j] = cal(mat[i][j:j + M])

    mattt = []
    for i in range(N):
        for j in range(N):
            mattt.append(matt[i][j])

    print(matt)
    print(mattt)

    ans = 0
    for i in range(len(mattt) - M):
        for j in range(i + M, len(mattt)):
            if ans < mattt[i] + mattt[j]:
                ans = mattt[i] + mattt[j]

    print("#%d" % tc, ans)
'''
