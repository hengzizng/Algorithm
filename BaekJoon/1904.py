# Solution 1 > list 사용
'''
N = int(input())

d = [0] * 1000001
d[1] = 1
d[2] = 2

for i in range(3, N + 1):
    # 나누지 않은 원래의 값으로 저장 시 메모리 초과 발생 주의
    d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[N])
'''

# Solution 2 > 두 변수 a, b를 사용
# Solution 1에 비해 메모리는 약 3/1, 시간은 약 2/1 정도로 줄어든다.
N = int(input())

a, b = 1, 1

for _ in range(N - 1):
    a, b = b, (a + b) % 15746

print(b)