import sys
sys.stdin = open("SWExpertAcademy/1225input.txt")

# 58,872 kb
# 메모리
# 165 ms
# 실행시간
# 432
# 코드길이

for _ in range(10):
    result = '#' + input()

    numbers = list(map(int, input().split()))
    cycle = 0
    index = -1
    while numbers[index] > 0:
        cycle = (cycle % 5) + 1
        index = (index + 1) % 8
        numbers[index] -= cycle

    for i in range(index + 1, 8):
        result += ' ' + str(numbers[i])
    for i in range(index):
        result += ' ' + str(numbers[i])
    result += ' 0'
    
    print(result)