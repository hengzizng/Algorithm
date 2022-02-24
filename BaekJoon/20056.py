# 66 min
# N: 격자 크기, M: 파이어볼 개수, K: 명령 수
# (r, c): 파이어볼 위치, m: 질량, d: 방향, s: 속력(이동 거리)

# fireballs = {(r, c) : [(m, d, s), ...], ...}
#
# 1. 파이어볼 이동 (N보다 커지면 1부터 다시 시작)
#    fireballs 의 keys 반복
#      fireballs[key] 반복
#        new_fireballs 에 이동한 파이어볼 추가
#
# 2. 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서
#    fireballs 의 keys 반복
#      2개 이상이 있는 key만 아래 과정 진행
#
#      fireballs[key] 반복으로
#      m(합쳐진 파이어볼 질량의 합/5), s(합쳐진 파이어볼 속력의 합/합쳐진 파이어볼의 개수) 구하기
#
#      m 0 이상 여부 판단
#
#      모두 홀수/짝수 여부 판단
#      모두 홀수이면 방향 0, 2, 4, 6 / 그렇지 않으면 방향 1, 3, 5, 7 으로 파이어볼 생성
#      new_fireballs에 추가

from collections import defaultdict
import sys
read = sys.stdin.readline


# 파이어볼 이동
def move(fireballs):
    new_fireballs = defaultdict(list)
    for key in fireballs.keys():
        for value in fireballs[key]:
            r = (key[0] + drdc[value[1]][0] * value[2]) % N
            c = (key[1] + drdc[value[1]][1] * value[2]) % N
            new_fireballs[(r, c)].append(value)
    return new_fireballs


# 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서
def do(fireballs):
    new_fireballs = defaultdict(list)
    for key in fireballs.keys():
        if len(fireballs[key]) == 1:
            new_fireballs[key] = fireballs[key]
            continue

        m, s = 0, 0
        d_flag = 0  # 방향을 판단하기 위한 변수(모두 짝수이면 0, 모두 홀수이면 len(fireballs[key]))
        for value in fireballs[key]:
            m += value[0]
            s += value[2]
            if value[1] % 2 == 1:
                d_flag += 1

        m = m // 5
        if m == 0:
            continue

        s = s // len(fireballs[key])
        d_flag = 0 if (d_flag == 0 or d_flag == len(fireballs[key])) else 1

        for d in next_d[d_flag]:
            new_fireballs[key].append((m, d, s))

    return new_fireballs


drdc = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
next_d = [[0, 2, 4, 6], [1, 3, 5, 7]]

# N: 격자 크기, M: 파이어볼 개수, K: 명령 수
N, M, K = map(int, read().split())
fireballs = defaultdict(list)
for _ in range(M):
    # (r, c): 파이어볼 위치, m: 질량, d: 방향, s: 속력(이동 거리)
    r, c, m, s, d = map(int, read().split())
    fireballs[(r - 1, c - 1)].append((m, d, s))

for _ in range(K):
    fireballs = move(fireballs)
    fireballs = do(fireballs)

m_sum = 0
for key in fireballs.keys():
    for value in fireballs[key]:
        m_sum += value[0]
print(m_sum)
