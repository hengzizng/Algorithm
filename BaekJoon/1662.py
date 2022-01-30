from collections import deque

# 1. 앞에서부터 괄호를 만나기 전까지의 문자열 길이를 string_length 변수에 저장
# 2. 여는 괄호를 만나면
# 2-1. string_length -= 1
# 2-2. stack에 string_length push
# 2-3. 여는 괄호 앞의 숫자 push, "(" push
# 3. 닫는 괄호를 만나면
# 3-1. string_length 를 push
# 3-2. "(" 나오기 전까지 계속 더해서 push

S = input()
stack = deque()
string_length = 0
for index in range(len(S)):
    if S[index] == "(":
        string_length -= 1

        stack.append(string_length)
        stack.append(int(S[index - 1]))
        stack.append("(")

        string_length = 0
    elif S[index] == ")":
        now_number = string_length
        while stack and stack[-1] != "(":
            now_number += stack.pop()

        stack.pop()
        stack.append(now_number * stack.pop())
        string_length = 0
    else:
        string_length += 1

while stack:
    string_length += stack.pop()

print(string_length)