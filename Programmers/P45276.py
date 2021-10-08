''' # 첫 번째 풀이
from collections import deque

def solution(participant, completion):
    """
    completion_q = deque(completion)
    
    while completion_q:
        participant.remove(completion_q.pop())
        
    return participant[0]
    """   
    
    participant.sort()
    completion.sort()
    participant_q = deque(participant)
    completion_q = deque(completion)
    
    for i in range(len(completion)):
        p = participant_q.popleft()
        if p != completion_q.popleft():
            return p
    
    return participant[-1]
'''
from collections import defaultdict


def solution(participant, completion):
    # 참가자 이름별로 개수를 센다.
    participant_counter = defaultdict(int)
    for p in participant:
        participant_counter[p] += 1
    
    # 완주한 이름별로 개수를 센다.
    completion_counter = defaultdict(int)
    for c in completion:
        completion_counter[c] += 1
    
    # 참가자 이름으로 반복문을 돌려서, 그 개수가 다르다면 return한다.
    for key, value in participant_counter.items():
        if completion_counter[key] != value:
            return key