from collections import deque
import sys
read = sys.stdin.readline


answers = []
T = int(read())
for _ in range(T):
    p = list(read().strip()) # 수행할 함수
    n = int(read()) # 배열에 들어있는 수의 개수
    x = read().strip()[1:-1] # 숫자 배열
    x = deque() if x == "" else deque(x.split(","))
    
    answer = ""
    is_reverse = False # 뒤집어졌는지 여부
    for command in p:
        if command == 'D': # 버리기 함수
            if x:
                if is_reverse:
                    x.pop()
                else:
                    x.popleft()
            else:
                answer = "error"
                break
        else: # 뒤집기 함수
            is_reverse = False if is_reverse else True
    
    if answer == "":
        answer += "["
        while x:
            if is_reverse:
                answer += x.pop()
            else:
                answer += x.popleft()
            if x:
                answer += ","
        answer += "]"
    answers.append(answer)

for answer in answers:
    print(answer)