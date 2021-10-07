def solution(price, money, count):
    # price: 놀이 기구 이용료
    # money: 처음 가지고 있던 금액
    # count: 이용 횟수
    
    for i in range(1, count + 1):
        money -= price * i

    answer = 0
    if money < 0:
        answer = money * -1

    return  answer


print(solution(3, 20, 4), 10)