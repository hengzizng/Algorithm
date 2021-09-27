def solution(numbers, target):
    def combination(index, value):
        if index == len(numbers):
            if value == target:
                answer[0] += 1
            return
        
        combination(index + 1, value + numbers[index])
        combination(index + 1, value - numbers[index])


    answer = [0]
    combination(0, 0)
    return answer[0]


print(solution([1, 1, 1, 1, 1], 3))