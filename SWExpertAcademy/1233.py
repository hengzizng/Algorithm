# 61,220 kb
# 메모리
# 205 ms
# 실행시간
# 636
# 코드길이

import sys
sys.stdin = open("TestCase/SWExpertAcademy/1233input.txt")

def is_number(target):
    if '0' <= target <= '9':
        return True
    else:
        return False

for tc in range(1, 10 + 1):
    N = int(input())
    is_available = '1'
    for n in range(N):
        node_info = list(input().split())

        if is_available == '0':
            continue

        # 리프노드가 아닌데 숫자이면 유효하지 않음
        if len(node_info) == 4 and is_number(node_info[1]):
            is_available = '0'
        # 리프노드인데 숫자가 아니면 유효하지 않음
        elif len(node_info) == 2 and not is_number(node_info[1]):
            is_available = '0'
    
    print("#" + str(tc) + " " + is_available)

