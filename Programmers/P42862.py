# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
def solution(n, lost, reserve):
    have_count = [1] * (n + 1) # 각 학생이 가지고 있는 체육복의 수
    
    # 도난당한 학생들
    for l in lost:
        have_count[l] -= 1
    
    # 여벌의 체육복을 가져온 학생들
    for r in reserve:
        have_count[r] += 1
    
    # 체육복을 빌려준다
    for student in range(1, n + 1):
        # 체육복이 2개일 때만 빌려준다
        if have_count[student] < 2:
            continue
        # 앞번호 학생이 체육복이 없다면 빌려준다
        if student > 1 and have_count[student - 1] == 0:
            have_count[student] -= 1
            have_count[student - 1] += 1
        # 뒷번호 학생이 체육복이 없다면 빌려준다
        elif student < n and have_count[student + 1] == 0:
            have_count[student] -= 1
            have_count[student + 1] += 1
    
    # 체육수업을 듣는 학생 수 count
    answer = 0
    for student in range(1, n + 1):
        if have_count[student] >= 1:
            answer += 1
    
    return answer



print(solution(4, [3, 1, 2], [2, 4, 3]), 3)