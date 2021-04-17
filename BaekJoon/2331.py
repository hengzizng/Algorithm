# A: 시작 숫자, P: 각 자리를 곱할 회수
A, P = map(int, input().split())
# D: 구한 수열 집합
D = set()
# D_list: 구한 수열 리스트
D_list = []

now = A
while now not in D:
    D.add(now)
    D_list.append(now)
    before = now

    quotient, now = now, 0
    while quotient > 0:
        quotient, remainder = quotient // 10, quotient % 10
        now += remainder ** P

repeat_start_index = D_list.index(now)
print(len(D_list[:repeat_start_index]))