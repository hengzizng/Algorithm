def solution(s):
    s = s[2:-2] # 앞, 뒤의 중괄호 2개씩 제거
    set_strs = s.split("},{") # 각 집합별로 분리
    set_strs.sort(key=lambda x: len(x)) # 각 집합의 길이를 기준으로 정렬
    
    # 각 집합의 원소들을 분리
    sets = []
    for set_str in set_strs:
        sets.append(set_str.split(","))
    
    answer = [] # s가 표현하는 튜플 (구하려는 답)
    is_check = set() # 체크한 원소들을 담는다.
    for now_set in sets: # 집합 반복문
        for now_num in now_set: # 원소 반복문
            now_num = int(now_num)
            if now_num not in is_check: # 현재 원소가 체크한 적 없는 원소라면
                is_check.add(now_num)
                answer.append(now_num)
                break
    
    return answer