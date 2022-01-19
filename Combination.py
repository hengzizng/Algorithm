'''
재귀로 조합을 생성하는 두 가지 방법의
함수 수행 횟수를 비교하는 코드입니다.
'''


import sys
read = sys.stdin.readline

def comb1(count, index, selected):
    recursion_count[0] += 1

    if count == M:
        print(selected)
        return
    
    if index == N:
        return
    
    selected[count] = index
    comb1(count + 1, index + 1, selected)
    comb1(count, index + 1, selected)


def comb2(count, start, selected):
    recursion_count[1] += 1

    if count == M:
        print(selected)
        return
    
    if start == N:
        return
    
    for i in range(start, N):
        selected[count] = i
        comb2(count + 1, i + 1, selected)


recursion_count = [0, 0]
N = 5
M = 3
comb1(0, 0, [-1] * M)
print("------------")
comb2(0, 0, [-1] * M)
print(recursion_count)