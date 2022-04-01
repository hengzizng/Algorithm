import sys
read = sys.stdin.readline


# 이번 자리에 넣을 연산자를 선택하고, 계산한다.
def calc(index, num, add_count, sub_count, mult_count, div_count):
    if index == N - 1: # 연산자의 개수는 N -1개
        max_min_value[0] = max(max_min_value[0], num)
        max_min_value[1] = min(max_min_value[1], num)
        return
    
    index += 1
    if add_count >= 1:
        calc(index, num + A[index], add_count - 1, sub_count, mult_count, div_count)
    if sub_count >= 1:
        calc(index, num - A[index], add_count, sub_count - 1, mult_count, div_count)
    if mult_count >= 1:
        calc(index, num * A[index], add_count, sub_count, mult_count - 1, div_count)
    if div_count >= 1 and A[index] != 0:
        flag = 0 if num == 0 else (num // abs(num))
        calc(index, abs(num) // A[index] * flag, add_count, sub_count, mult_count, div_count - 1)



# N: 수의 개수, A: 수열
N, A = int(read()), list(map(int, read().split()))
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
add_count, sub_count, mult_count, div_count = map(int, read().split())

max_min_value = [-1 * (10 ** 9), 10 ** 9]

calc(0, A[0], add_count, sub_count, mult_count, div_count)

print(max_min_value[0])
print(max_min_value[1])