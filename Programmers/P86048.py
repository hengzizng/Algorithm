'''
# 더 효율적인 방법
def solution(enter, leave):
    answer = [0] * len(enter)

    room = set()
    enter_index = 0
    for person in leave:
        while person not in room:
            room.append(enter[enter_index])
            enter_index += 1
        room.remove(person)
        for left_person in room:
            answer[left_person - 1] += 1
        answer[person - 1] += len(room)

    return answer
'''

# 내 풀이
def solution(enter, leave):
    def count_up(room): # 방 안에 있는 사람들의 count를 1씩 증가시킴
        for person in room:
            answer[person] += 1
    
    answer = [0] * (len(enter) + 1)
    room, visited = set(), set()
    for person in leave: # 나온 순으로 반복
        for enter_person in enter: # 나온 사람이 들어갈 때까지 탐색
            if enter_person not in visited and enter_person not in room: # 새로운 사람이 들어가면 (방문하지 않았던)
                count_up(room) # 기존에 있던 사람들 count 1씩 증가시킴
                answer[enter_person] = len(room) # 새로 추가된 사람은 안에 있는 인원만큼으로 count 설정
                room.add(enter_person)
                visited.add(enter_person)
            
            if enter_person == person:
                break
        
        room.remove(person)
    
    return answer[1:]