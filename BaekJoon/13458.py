# N: 시험장 수, A[i]: i번 시험장에 있는 응시자 수
# B / C: 총 / 부 감독관이 한 시험장에서 감시할 수 있는 응시자의 수
# 각 시험장에 총감독관은 1명만, 부감독관은 여러명 가능
import sys
read = sys.stdin.readline


N = int(read())
A = list(map(int, read().split()))
B, C = map(int, read().split())

min_count = 0  # 감독관의 최소 수
for i in range(N):  # 시험장 수만큼 반복
    temp = 0 if A[i] - B < 0 else A[i] - B  # 총감독관이 감독할 수 있는 수를 제외한 응시자의 수
    min_count += 1 + (temp // C) + (0 if temp % C == 0 else 1)

print(min_count)
