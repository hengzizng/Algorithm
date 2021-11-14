def solution(left, right):
    answer = 0
    
    for number in range(left, right + 1):
        # 약수의 개수가 홀수가 나올 경우는 제곱근으로 딱 나누어떨어지는 경우밖에 없음
        root = int(number ** 0.5)
        if root ** 2 == number:
            number *= -1

        answer += number

    return answer