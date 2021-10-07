def solution(weights, head2head):
    results = [] # 각 복서별 정보 : (승률, 자신보다 무거운 복서를 이긴 횟수, 자신의 몸무게, 번호 * -1)
    
    for person, weight in enumerate(weights): # 복서별로 반복
        win_count, match_count = 0, 0 # 이긴 횟수, 경기 횟수
        heavy_win_count = 0 # 자신보다 무거운 복서를 이긴 횟수
        
        for opponent, result in enumerate(head2head[person]): # 승패 결과별로 반복
            if result == 'N': # 경기를 하지 않았으면 볼 필요 없음
                continue
            
            match_count += 1
            if result == 'W': # 이겼으면
                win_count += 1
                if weight < weights[opponent]: # 자신보다 무거운 복서이면
                    heavy_win_count += 1
        
        win_rate = 0 if win_count == 0 else win_count / match_count
        results.append((win_rate, heavy_win_count, weight, person * -1))
    
    results.sort(reverse = True) # 네 가지 조건 한번에 정렬
    
    answer = []
    for result in results:
        answer.append((result[3] * -1) + 1) # 복서를 인덱스로 사용했기 때문에 1 더해줌
    
    return answer