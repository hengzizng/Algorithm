import sys
read = sys.stdin.readline


# N: 전체 용액의 수
N = int(read())
# 각 용액의 특성값
numbers = list(map(int, read().split()))
# 왼쪽, 오른쪽 포인터
left, right = 0, N - 1
# [용액 값 인덱스1, 용액 값 인덱스 2, 0과 가까운 혼합 특성값]
zero_info = [left, right, numbers[left] + numbers[right]]

while left < right:
    mix_val = numbers[left] + numbers[right]

    if abs(mix_val) < abs(zero_info[2]):
        zero_info = [left, right, mix_val]
    
    if mix_val == 0:
        break
    elif mix_val < 0:
        left += 1
    else:
        right -= 1

print(numbers[zero_info[0]], numbers[zero_info[1]])