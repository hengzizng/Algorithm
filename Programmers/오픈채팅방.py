# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.03ms, 10MB)
# 테스트 4 〉	통과 (0.04ms, 10.1MB)
# 테스트 5 〉	통과 (0.61ms, 10.4MB)
# 테스트 6 〉	통과 (1.11ms, 10.4MB)
# 테스트 7 〉	통과 (0.94ms, 10.3MB)
# 테스트 8 〉	통과 (0.66ms, 10.5MB)
# 테스트 9 〉	통과 (0.76ms, 10.5MB)
# 테스트 10 〉	통과 (0.69ms, 10.5MB)
# 테스트 11 〉	통과 (0.39ms, 10.2MB)
# 테스트 12 〉	통과 (0.38ms, 10.2MB)
# 테스트 13 〉	통과 (0.70ms, 10.4MB)
# 테스트 14 〉	통과 (0.77ms, 10.5MB)
# 테스트 15 〉	통과 (0.01ms, 9.98MB)
# 테스트 16 〉	통과 (0.01ms, 10MB)
# 테스트 17 〉	통과 (0.07ms, 10.2MB)
# 테스트 18 〉	통과 (0.06ms, 10.1MB)
# 테스트 19 〉	통과 (0.77ms, 10.5MB)
# 테스트 20 〉	통과 (0.56ms, 10.3MB)
# 테스트 21 〉	통과 (0.52ms, 10.4MB)
# 테스트 22 〉	통과 (0.56ms, 10.3MB)
# 테스트 23 〉	통과 (0.70ms, 10.5MB)
# 테스트 24 〉	통과 (0.79ms, 10.7MB)
# 테스트 25 〉	통과 (99.29ms, 59.5MB)
# 테스트 26 〉	통과 (140.77ms, 66.9MB)
# 테스트 27 〉	통과 (123.22ms, 68.7MB)
# 테스트 28 〉	통과 (127.42ms, 71.1MB)
# 테스트 29 〉	통과 (162.09ms, 70.8MB)
# 테스트 30 〉	통과 (79.09ms, 55.7MB)
# 테스트 31 〉	통과 (102.90ms, 68.6MB)
# 테스트 32 〉	통과 (78.77ms, 60.9MB)

def solution(record):
    msg_map = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    id_map = {} # {유저 아이디 : 닉네임}
    answer = []

    for now in record:
        now = now.split() # now : [진행한 작업, 유저 아이디, 닉네임]
        if now[0] in msg_map:
            answer.append([now[0], now[1]])
        if len(now) > 2: # Leave일때는 닉네임 새로 넣어줄 필요 없다.
            id_map[now[1]] = now[2]

    # now : [진행한 작업, 유저 아이디]
    for index, now in enumerate(answer):
        answer[index] = id_map[now[1]] + msg_map[now[0]]

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))