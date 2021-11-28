def solution(numbers):
    numbers.sort()
    sums = set()
    
    for left in range(len(numbers)):
        for right in range(left + 1, len(numbers)):            
            sums.add(numbers[left] + numbers[right])
    
    sums = list(sums)
    sums.sort()
    
    return sums