from collections import deque
import sys
read = sys.stdin.readline


def commandD(n):
    return n * 2 % 10000

def commandS(n):
    if n == 0:
        return 9999
    else:
        return n - 1

def commandL(n):
    return (n // 1000) + ((n % 1000) * 10)

def commandR(n):
    return ((n % 10) * 1000) + (n // 10)

def getMinCommand(initial, final):
    if initial == final:
        return ""

    queue = deque([initial])
    path = [''] * 10000
    path[initial] = 'P'

    while queue:
        num = queue.popleft()
        
        next_num = commandD(num)
        if path[next_num] == '':
            path[next_num] = path[num] + "D"
            if next_num == final:
                return path[next_num]
            queue.append(next_num)
        
        next_num = commandS(num)
        if path[next_num] == '':
            path[next_num] = path[num] + "S"
            if next_num == final:
                return path[next_num]
            queue.append(next_num)
        
        next_num = commandL(num)
        if path[next_num] == '':
            path[next_num] = path[num] + "L"
            if next_num == final:
                return path[next_num]
            queue.append(next_num)
        
        next_num = commandR(num)
        if path[next_num] == '':
            path[next_num] = path[num] + "R"
            if next_num == final:
                return path[next_num]
            queue.append(next_num)

T = int(read())
answers = []

for t in range(T):
    initial, final = map(int, read().split())
    answers.append(getMinCommand(initial, final))

for answer in answers:
    print(answer[1:])