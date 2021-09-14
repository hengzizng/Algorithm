import re

# 정규식 사용
# 테스트 1 〉	통과 (0.13ms, 10MB)
# 테스트 2 〉	통과 (0.13ms, 10.1MB)
# 테스트 3 〉	통과 (0.13ms, 9.96MB)
# 테스트 4 〉	통과 (0.12ms, 9.94MB)
# 테스트 5 〉	통과 (0.13ms, 10MB)
# 테스트 6 〉	통과 (0.13ms, 10.1MB)
# 테스트 7 〉	통과 (0.13ms, 9.96MB)
# 테스트 8 〉	통과 (0.13ms, 9.98MB)
# 테스트 9 〉	통과 (0.13ms, 9.98MB)
# 테스트 10 〉	통과 (0.13ms, 10.1MB)
# 테스트 11 〉	통과 (0.13ms, 10MB)
# 테스트 12 〉	통과 (0.14ms, 10MB)
# 테스트 13 〉	통과 (0.14ms, 9.99MB)
# 테스트 14 〉	통과 (0.13ms, 10.1MB)
# 테스트 15 〉	통과 (0.13ms, 9.95MB)
# 테스트 16 〉	통과 (0.13ms, 10MB)
# 테스트 17 〉	통과 (0.15ms, 10.1MB)
# 테스트 18 〉	통과 (0.16ms, 9.99MB)
# 테스트 19 〉	통과 (0.20ms, 9.98MB)
# 테스트 20 〉	통과 (0.22ms, 10MB)
# 테스트 21 〉	통과 (0.21ms, 10.1MB)
# 테스트 22 〉	통과 (0.23ms, 10.1MB)
# 테스트 23 〉	통과 (0.14ms, 10MB)
# 테스트 24 〉	통과 (0.14ms, 10.3MB)
# 테스트 25 〉	통과 (0.15ms, 9.96MB)
# 테스트 26 〉	통과 (0.14ms, 9.96MB)
def solution1(new_id):

    # step 1
    recommend_id = new_id.lower()
    # step 2
    recommend_id = re.sub('[^a-z0-9-_.]', '', recommend_id)
    # step 3
    recommend_id = re.sub('[.]+', '.', recommend_id)
    # step 4
    recommend_id = recommend_id.strip('.')
    # step 5
    if not recommend_id:
        recommend_id = 'a'
    # step 6
    length = len(recommend_id)
    if length >= 16:
        recommend_id = recommend_id[:14] if recommend_id[14] == '.' else recommend_id[:15]
    # step 7
    length = len(recommend_id)
    recommend_id += recommend_id[-1] * (3-length)

    return recommend_id


# 일반 풀이
# 테스트 1 〉	통과 (0.01ms, 10MB)
# 테스트 2 〉	통과 (0.01ms, 9.91MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 9.98MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)
# 테스트 15 〉	통과 (0.02ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.1MB)
# 테스트 18 〉	통과 (0.04ms, 10.1MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)
# 테스트 20 〉	통과 (0.17ms, 10.1MB)
# 테스트 21 〉	통과 (0.16ms, 10.2MB)
# 테스트 22 〉	통과 (0.27ms, 10.1MB)
# 테스트 23 〉	통과 (0.04ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.1MB)
# 테스트 25 〉	통과 (0.07ms, 10.2MB)
# 테스트 26 〉	통과 (0.04ms, 10MB)
def solution2(new_id):
    def valid(char):
        if "a" <= char <= "z":
            return True
        if "0" <= char <= "9":
            return True
        if char == "." or char == "_" or char == "-":
            return True
        return False
        
    length = 0
    recommand_id = ""
    
    for char in new_id:
        if char == ".":
            if length == 0 or recommand_id[length - 1] == ".":
                continue
        
        char = char.lower()
        if not valid(char):
            continue
        
        length += 1
        recommand_id += char
        
        if length == 15:
            break
    
    
    if length == 0:
        length = 1
        recommand_id = "a"
        
    while recommand_id[length - 1] == ".":
        length -= 1
    recommand_id = recommand_id[:length]
    
    while length < 3:
        recommand_id += recommand_id[length - 1]
        length += 1
    
    return recommand_id