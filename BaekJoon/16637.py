import sys
read = sys.stdin.readline


# 괄호를 추가할 연산자의 인덱스를 선택
def select(index, selected):
    if index >= N // 2:
        result = get_result(selected)
        max_value[0] = max(result, max_value[0])
        return

    # 괄호 추가 O
    selected[index] = True
    select(index + 2, selected)
    # 괄호 추가 X
    selected[index] = False
    select(index + 1, selected)


# 추가한 괄호에 따라 수식의 결과를 계산
def get_result(selected):
    result = 0
    expression = ['+']

    # 괄호 연산자 먼저 처리
    index = 0
    while index < N // 2:
        # 괄호 내 연산자이면
        if selected[index]:
            expression.append(calculate(operations[index], numbers[index], numbers[index + 1]))
            index += 1
        # 괄호 없는 연산자라면
        else:
            expression.append(numbers[index])

        # 마지막 연산자였다면
        if index == N // 2:
            break
    
        expression.append(operations[index])
        index += 1

    # 마지막 연산자에 괄호가 없었을 경우 마지막 숫자 추가
    if not selected[index - 1]:
        expression.append(numbers[index])

    # 괄호가 없는 나머지 수식 처리
    for index in range(0, len(expression), 2):
        result = calculate(expression[index], result, expression[index + 1])

    return result


# 연산자로 계산한 결과를 반환
def calculate(operation, number1, number2):
    if operation == '+':
        return number1 + number2
    if operation == '-':
        return number1 - number2
    if operation == '*':
        return number1 * number2


N = int(read())  # 수식의 길이
expression = read().strip()  # 수식
max_value = [-1 * (2 ** 31)]

numbers, operations = [], []  # 수식 내 숫자, 연산자
for index in range(N):
    if index % 2 == 0:
        numbers.append(int(expression[index]))
    else:
        operations.append(expression[index])

if N == 1:
    max_value[0] = expression
else:
    select(0, [False] * (N // 2))

print(max_value[0])
