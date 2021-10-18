# solution 1
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.05ms, 10.3MB)
# 테스트 12 〉	통과 (0.07ms, 10.3MB)
# 테스트 13 〉	통과 (0.08ms, 10.3MB)
# 테스트 14 〉	통과 (0.13ms, 10.2MB)
# 테스트 15 〉	통과 (0.18ms, 10.2MB)
# 테스트 16 〉	통과 (0.42ms, 10.2MB)
# 테스트 17 〉	통과 (0.36ms, 10.2MB)
# 테스트 18 〉	통과 (0.57ms, 10.2MB)
# 테스트 19 〉	통과 (0.80ms, 10.3MB)
# 테스트 20 〉	통과 (0.65ms, 10.3MB)
# 테스트 21 〉	통과 (0.66ms, 10.3MB)
# 테스트 22 〉	통과 (0.32ms, 10.3MB)
# 테스트 23 〉	통과 (0.51ms, 10.2MB)
# 테스트 24 〉	통과 (0.22ms, 10.2MB)
# 테스트 25 〉	통과 (0.40ms, 10.3MB)

# 올바른 문자열이면 True를 반환하는 함수
def is_right(parens):
    stack = []
    
    for paren in parens:
        if stack and paren == ')':
            stack.pop()
        else:
            stack.append(paren)
    
    return len(stack) == 0

def solution(p):
    pair = {'(': ')', ')': '('}
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if not p:
        return p

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    stack = []
    u, v = "", ""
    for i in range(len(p)):
        if stack and p[i] != stack[-1]:
            stack.pop()
        else:
            stack.append(p[i])
        u += p[i]
            
        if not stack:
            if i < len(p) - 1:
                v = p[i+1:]
            break
    
    # 3. u가 "올바른 괄호 문자열" 이라면 v에 대해 1단계부터 다시 수행
    if is_right(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환
        return u + solution(v)
    
    # 4. u가 "올바른 괄호 문자열"이 아니라면
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙임
        new = '('
        # 4-2. v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
        new += solution(v)
        # 4-3. ')'를 다시 붙임
        new += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        for i in range(1, len(u)-1):
            new += pair[u[i]]
        
    # 4-5. 생성된 문자열을 반환
    return new