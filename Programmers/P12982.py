def solution(d, budget):
    d.sort()
    
    support_price = 0
    for support_count, price in enumerate(d, 1):
        support_price += price # 일단 현재 신청 금액을 더한다
        if support_price > budget: # 방금 만든 값이 예산보다 크다면 종료
            break
            
    if support_price > budget: # 조건에 걸려서 나온 경우에만 1을 빼준다
        support_count -= 1
            
    return support_count