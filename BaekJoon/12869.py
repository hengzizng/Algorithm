import sys
read = sys.stdin.readline


# SCV1 >= SCV2 >= SCV3
def attack(attack_count, SCV1, SCV2, SCV3):
    # 체력이 같은 이미 구한 공격 횟수보다 많거나 같을 경우
    if attack_count >= attack_counts[SCV1][SCV2][SCV3]:
        return

    # 최소 공격 횟수 갱신
    attack_counts[SCV1][SCV2][SCV3] = attack_count

    # 공격 값 순열에 따라 공격
    for values in attack_map:
        # 각각 공격 값에 따라 체력을 감소시키고, 정렬
        temp = [SCV1 - values[0], SCV2 - values[1], SCV3 - values[2]]
        temp.sort()
        # 0 미만일 경우 0으로 통일
        for i in range(3):
            if temp[i] < 0:
                temp[i] = 0
            else:
                break

        attack(attack_count + 1, temp[2], temp[1], temp[0])


# 공격 값 순열
attack_map = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]
N = int(read())  # SCV의 수
SCVs = list(map(int, read().split())) + ([0] * (3 - N))  # SCV의 체력

# 내림차순 정렬 ([0][1][2]와 [2][0]][1]의 값은 같아야 하기 때문에 내림차순으로 통일)
SCVs.sort(reverse=True)

# 남아있는 체력에 따른 최소 공격 횟수
# attack_counts[i][j][k] : i, j, k만큼 체력이 남았을 때 최소 공격 횟수
attack_counts = [[[60] * 61 for _ in range(61)] for _ in range(61)]

# 공격 시작
attack(0, SCVs[0], SCVs[1], SCVs[2])

print(attack_counts[0][0][0])
