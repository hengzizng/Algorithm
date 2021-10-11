def solution(answers):
    selections = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    pointer = [0, 0, 0] # 각 수포자 별 selections 인덱스 포인터
    scores = [0, 0, 0] # 각 수포자 별 점수
    
    for answer in answers:
        for i in range(3): # 수포자 별로 반복
            if selections[i][pointer[i]] == answer:
                scores[i] += 1
            pointer[i] = (pointer[i] + 1) % len(selections[i])
    
    answer = []
    max_score = max(scores)
    for person, score in enumerate(scores, 1):
        if score == max_score:
            answer.append(person)
    
    return answer