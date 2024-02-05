import sys
read = sys.stdin.readline


# 현재 자릿수(i)의 숫자로 만들 숫자 선택
# left_led: 바꿀 수 있는 남은 LED 개수
def select(left_led, i, now_number):
    if left_led < 0 or now_number > N:
        return
    
    if i == K:
        # 변경할 숫자는 1 이상
        if now_number > 0:
            case_count[0] += 1
        return
    
    # k: 변경할 숫자
    for k in range(10):
        select(left_led - counts[number[i]][k], i + 1, now_number + (10 ** i) * k)


# 1 이상 N 이하 만큼의 숫자로 변경 예정
# K: 자릿수
# P: 반전시킬 LED의 최대 수
# X: 실제 층
N, K, P, X = map(int, read().split())

# leds[i]: 숫자 i의 LED 상태
leds = [[1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1]]

# counts[i][j]: 숫자 i에서 j로 변경하는데 필요한 반전 LED 개수
counts = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(i + 1, 10, 1):
        count = 0
        for k in range(7):
            if leds[i][k] != leds[j][k]:
                count += 1
        counts[i][j] = count
        counts[j][i] = count

# 각 자릿수별로 숫자(number[i]: i의자리 숫자)
number, max_number = [0] * K, [0] * K
temp_X, temp_N = X, N
for i in range(K - 1, 0 - 1, -1):
    number[i] = temp_X // (10 ** i)
    temp_X = temp_X % (10 ** i)
    max_number[i] = temp_N // (10 ** i)
    temp_N = temp_N % (10 ** i)

# 변경할 수 있는 경우의 수
case_count = [0]

# 변경할 숫자 선택
select(P, 0, 0)

# 숫자를 하나도 바꾸지 않았을 경우를 제외
print(case_count[0] - 1)
