from collections import deque


def solution(s):
    stack = deque()

    for char in s:
        # 스택이 비어있거나 peek가 현재 글자와 다르다면 push
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    return 0 if stack else 1

print(solution("baabaa"), 1)
print(solution("cdcd"), 0)