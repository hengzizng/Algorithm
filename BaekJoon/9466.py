# Solution 1 > 시간초과 발생
'''
from collections import deque


def get_students_in_team(start_node):
    stack = deque([start_node])
    checked = set()
    checked_list = []

    while stack:
        now_node = stack.pop()
        if now_node not in checked:
            checked.add(now_node)
            checked_list.append(now_node)
            stack.append(selections[now_node])
        else:
            temp = checked_list.index(now_node)
            return set(checked_list[temp:])
    
    return set()


# T: 테스트 케이스의 수
T = int(input())
answer = [0 for _ in range(T)]

for test in range(T):
    n = int(input())
    rest_students = set(list(range(1, n)))
    selections = [0] + list(map(int, input().split()))

    for selection in selections[1:]:
        if selection in rest_students:
            rest_students = rest_students - get_students_in_team(selection)
    
    answer[test] = len(rest_students)

for rest_num in answer:
    print(rest_num)
'''


# Solution 2 > 정답

from collections import deque
from sys import stdin

read = stdin.readline


def set_student_position(start_node, students_status):
    if start_node == selections[start_node]:
        students_status[start_node] = 1
        return

    stack = deque([start_node])
    # checked: {학생번호 : 체크된 순서, ...}
    checked = {}
    # check_no: 학생이 체크된 순서 list (index: 순서, value: 학생번호)
    check_no = []

    while stack:
        now_node = stack.pop()
        if now_node in checked:
            order = checked[now_node]
            for student in check_no[order:]:
                students_status[student] = 1
            break
        else:
            stack.append(selections[now_node])
            checked[now_node] = len(check_no)
            check_no.append(now_node)
            students_status[now_node] = 0


# T: 테스트 케이스의 수
T = int(read())
answer = [0 for _ in range(T)]

for test in range(T):
    # n: 학생의 수
    n = int(read())
    selections = [0] + list(map(int, read().split()))
    # students_status: 학생이 팀에 속했는지 여부 (1: 속함, 0: 속하지 않음)
    students_status = {}

    for student in range(1, n+1):
        if student not in students_status:
            if selections[student] in students_status:
                students_status[student] = 0
            else:
                set_student_position(student, students_status)
    
    for value in students_status.values():
        if not value:
            answer[test] += 1

for rest_num in answer:
    print(rest_num)