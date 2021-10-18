# 61,752 kb
# 메모리
# 203 ms
# 실행시간
# 467
# 코드길이


from collections import deque
import sys
sys.stdin = open("TestCase/SWExpertAcademy/1218input.txt")

brackets = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}

for tc in range(1, 10 + 1):
    length = int(input())
    chars = list(input())
    stack = deque()
    for char in chars:
        if stack and char in brackets.keys() and stack[-1] == brackets[char]:
            stack.pop()
        else:
            stack.append(char)
        
    if stack:
        print('#' + str(tc) + ' 0')
    else:
        print('#' + str(tc) + ' 1')
    