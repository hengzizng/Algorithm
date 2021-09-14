# 테스트 1 〉	통과 (0.02ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.5MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.5MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)

def solution(s):
    def is_number(char):
        if "0" <= char <= "9":
            return True
        else:
            return False

    numbers_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = ""
    word = ""
    for char in s:
        if is_number(char):
            answer += char
        else:
            word += char
            if word in numbers_map:
                answer += numbers_map[word]
                word = ""

    return int(answer)


print(solution("two000000000"))