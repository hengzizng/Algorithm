def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    duplicated = lost & reserve
    lost -= duplicated
    reserve -= duplicated
    
    answer = n - len(lost)
    
    for student in lost:
        if student - 1 in reserve:
            reserve.remove(student - 1)
        elif student + 1 in reserve:
            reserve.remove(student + 1)
        else:
            continue
        
        answer += 1
    
    return n - len(lost)


print(solution(4, [3, 1, 2], [2, 4, 3]), 3)