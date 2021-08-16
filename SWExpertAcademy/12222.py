# SW Expert Academy에는 파일입출력 사용 불가능 -> input 사용
# import sys
# read = sys.stdin.readline


TC = int(input())
answers = []  # 부분 문자열의 개수(K)를 담아두는 배열
for _ in range(TC):
    S = input()
    now = ""  # 현재 처리중인 문자열
    past = ""  # 직전에 처리한 문자열
    pointer = 0  # 현재 문자
    K = 0
    for pointer in range(len(S)):
        if past == now:
            now += S[pointer]
            continue
        K += 1
        past = now
        now = S[pointer]
    if past != now:
        K += 1
    answers.append(K)

for tc in range(1, TC + 1):
    print("#" + str(tc) + " " + str(answers[tc - 1]))