def solution(progresses, speeds):
    answers = []

    count = len(progresses) # 개발중인 기능의 개수 (for문에 사용)
    pointer = 0 # 가장 먼저 배포되어야 할 기능을 가리킨다.
    while pointer < count:
        for i in range(pointer, count): # 하루씩 작업한다.
            progresses[i] += speeds[i]
        
        answer = 0
        for i in range(pointer, count): # 오늘 배포할 수 있는 기능 개수를 구한다.
            if progresses[i] < 100:
                break
            answer += 1
        
        if answer > 0: # 배포할 수 있는 기능이 있다면
            pointer += answer
            answers.append(answer)

    return answers


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds), [2, 1])

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds), [1, 3, 2])