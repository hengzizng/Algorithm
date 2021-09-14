# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.47ms, 10.2MB)
# 테스트 3 〉	통과 (0.25ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.05ms, 10.1MB)
# 테스트 7 〉	통과 (0.51ms, 10.1MB)
# 테스트 8 〉	통과 (0.55ms, 10.2MB)
# 테스트 9 〉	통과 (1.53ms, 10.2MB)
# 테스트 10 〉	통과 (3.23ms, 10.1MB)
# 테스트 11 〉	통과 (0.13ms, 10.1MB)
# 테스트 12 〉	통과 (0.21ms, 10.1MB)
# 테스트 13 〉	통과 (0.14ms, 10.2MB)
# 테스트 14 〉	통과 (0.79ms, 10.1MB)
# 테스트 15 〉	통과 (0.13ms, 10.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.1MB)
# 테스트 17 〉	통과 (1.48ms, 10.2MB)
# 테스트 18 〉	통과 (1.45ms, 10MB)
# 테스트 19 〉	통과 (2.43ms, 10.1MB)
# 테스트 20 〉	통과 (3.19ms, 10.1MB)
# 테스트 21 〉	통과 (3.39ms, 10.1MB)
# 테스트 22 〉	통과 (6.24ms, 10.1MB)
# 테스트 23 〉	통과 (3.27ms, 10.1MB)
# 테스트 24 〉	통과 (2.91ms, 10.1MB)
# 테스트 25 〉	통과 (3.18ms, 10.1MB)
# 테스트 26 〉	통과 (5.63ms, 10.2MB)
# 테스트 27 〉	통과 (3.40ms, 10.1MB)
# 테스트 28 〉	통과 (0.02ms, 10.1MB)
def solution1(s):
    sLen = len(s)
    answer = sLen
    ansStr = ""
    
    for unitNum in range(1, (int(sLen/2)+1 if sLen%2 == 1 else int(sLen/2)+1)):
        repNum = 1
        idx = 0
        repStr = s[:unitNum]
        ansStr = ""
        
        while idx < sLen-unitNum:
            
            if s[idx:idx+unitNum] == s[idx+unitNum:idx+(2*unitNum)]:
                repStr = s[idx:idx+unitNum]
                repNum = repNum + 1
            else:
                ansStr = ansStr + (("" if repNum == 1 else str(repNum)) + s[idx:idx+unitNum])
                repNum = 1
            idx = idx + unitNum
        ansStr = ansStr + ("" if repNum == 1 else str(repNum)) + s[idx:]
        
        if answer > len(ansStr):
            answer = len(ansStr)
        
    return answer