from collections import defaultdict


def solution(table, languages, preference):
    answer, max_score = '', 0
    
    # 총합이 같은 직업군이 여러 개일 경우, 이름이 사전 순으로 가장 빠른 것을 찾기 위해 정렬
    table.sort()
    
    for score_string in table: # 각 직업군별로 확인
        temp = score_string.split()
        
        job = temp[0] # 이번에 확인할 직업군
        score_by_language = defaultdict(int) # 이번 직업군의 언어 별 점수 {언어 : 점수} 형태로 저장
        for i in range(1, 5 + 1):
            score_by_language[temp[i]] = 6 - i
        
        total_score = 0 # 이번 직업군 점수의 총 합
        for i in range(len(languages)):
            language = languages[i]
            total_score += score_by_language[language] * preference[i]
            
        if max_score < total_score: # 이름이 사전 순으로 오름차순 정렬 되어있으므로 같은 경우는 포함하지 않는다
            max_score = total_score
            answer = job
    
    return answer