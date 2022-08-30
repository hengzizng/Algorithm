import sys
read = sys.stdin.readline


def exercise(count, weight, used):
    if weight < 0:
        return

    if count == N:
        answer[0] += 1
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            exercise(count + 1, weight - K + A[i], used)
            used[i] = False


# N: 목표 일 수(운동키트 수), K: 하루에 줄어드는 중량
N, K = map(int, read().split())
# A: 중량 증가량 리스트
A = list(map(int, read().split()))
# answer: 운동 기간동안 항상 중량이 500 이상 되도록 하는 경우의 수
answer = [0]

exercise(0, 0, [False] * N)

print(answer[0])
