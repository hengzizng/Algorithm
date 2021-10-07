def solution(word):
    def get_count(target_length, length, compared):
        if compared > word: # 이미 만들어진 단어가 목표 단어보다 크다면 더이상 볼 필요 없음
            return
        
        if length == target_length: # 목표 길이만큼 단어 완성했으면
            count[0] += 1 # 이미 목표 단어보다 큰 단어들은 걸러졌기 때문에 그냥 더해준다
            return
        
        for alphabet in alphabets:
            get_count(target_length, length + 1, compared + alphabet)
    
    
    alphabets = ['A', 'E', 'I', 'O', 'U']
    count = [0]
    
    for target_length in range(1, 5 + 1): # 한자리 단어부터 다섯자리 단어까지 확인
        get_count(target_length, 0, "")
    
    return count[0]