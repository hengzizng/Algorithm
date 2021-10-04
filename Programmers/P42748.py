def solution(array, commands):
    answer = []

    for i, j, k in commands:
        i, j, k = i - 1, j - 1, k - 1 # 인덱스로 사용하기 위해 1씩 빼준다
        new_array = array[i : j + 1]
        new_array.sort()
        answer.append(new_array[k])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands), [5, 6, 3])