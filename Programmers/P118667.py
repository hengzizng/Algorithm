from collections import deque


def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    sum1, sum2 = sum(queue1), sum(queue2)
    for count in range((len(queue1) + len(queue2)) * 2):
        if sum1 == sum2:
            return count
        
        if sum1 > sum2:
            num = deque1.popleft()
            sum1 -= num
            
            deque2.append(num)
            sum2 += num
        else:
            num = deque2.popleft()
            sum2 -= num
            
            deque1.append(num)
            sum1 += num
            
    return -1