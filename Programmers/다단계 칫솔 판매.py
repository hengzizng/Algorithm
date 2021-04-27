from collections import defaultdict


def solution(enroll, referral, seller, amount):
    def set_profits(person, profit):
        while profit > 0 and person != '-':
            temp = profit - int(profit * 0.1)
            profits[person] += temp
            profit -= temp
            person = graph[person]

        
    # graph: {판매원 : 추천인}
    graph = {}
    # profits: {판매원 : 수익}
    profits = defaultdict(int)
    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        set_profits(seller[i], (amount[i] * 100))
        
    answer = []
    for person in enroll:
        answer.append(profits[person])
        
    return answer