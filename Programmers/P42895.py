"""
def solution(N, number):
    # D = [float('inf')] * 32001
    D = [float('inf')] * (number + 1)
    D[0] = 2 # N - N
    D[1] = 2 # N / N
    D[N - 1] = 4 # (N * N - N) / N
    D[N] = 1
    for now in range(2, number + 1):
        # case1
        D[now] = min(D[now], D[now - 1] + 2)
        
        # case2
        if (now > 1) and ((now - 1) % N != 0):
            # print("case2, D[now])
            D[now] = min(D[now], D[now - 1] + 1)
        
        # case3
        if now > N:
            # print("case2", D[now])
            D[now] = min(D[now], D[now - N] + 1)

        # case4
        if (now % N == 0) and (now > N):
            # print("case3", D[now])
            D[now] = min(D[now], D[now // N] + 1)
        
        # case6
        if now > 9:
            temp = str(now)
            isN = True
            for char in temp:
                if char != "1":
                    isN = False
                    break
            if isN:
                D[now] = min(D[now], D[int(temp[1:])] + 1)
        
        if D[now] > 8:
            D[now] = float('inf')
        
        if now != N: # case5
            D[now - 1] = min(D[now - 1], D[now] + 2)
        # print(">", now, D[now])
    
    # print(D)
    return -1 if D[number] == float('inf') else D[number]
"""

"""
from collections import deque


def solution(N, number):
    D = [float('inf')] * (N * number + 1)
    queue = deque()

    # N 1개
    queue.append((N, 1))

    while queue:
        now_number, count = queue.popleft()

        if now_number <= 0 or now_number > N * number or D[now_number] <= count:
            continue
            
        D[now_number] = count

        if now_number == number or count == 9: # count가 9이면 N 8개로 만들 수 있는 수는 끝났다.
            break

        count += 1
        queue.append((now_number + N, count))
        queue.append((now_number - N, count))
        queue.append((N - now_number, count))
        queue.append((now_number * N, count))
        if now_number / N == now_number // N: # 나눴을 때 정수이면
            queue.append((now_number // N, count))
        if N / now_number == N // now_number: # 나눴을 때 정수이면
            queue.append((N // now_number, count))

        temp = N
        for c in range(1, count):
            temp += N * (10 ** c)
        queue.append((temp, count))

    # print(D[:13])
    return -1 if D[number] == float('inf') else D[number]
"""



def solution(N, number):
    if number == N:
        return 1

    D = [set() for _ in range(9)] # N을 index 개수만큼 사용해서 만들 수 있는 수
    
    D[1].add(N)
    for count in range(2, 8 + 1): # N을 8개까지만 사용한다.
        temp = N
        for c in range(1, count):
            temp += N * (10 ** c)
        D[count].add(temp)

        if temp == number:
            return count

        # N count개 사용 : part1 + part2
        # N 2개 사용 : 1개 + 1개
        # N 3개 사용 : 1개 + 2개
        # N 4개 사용 : 1개 + 3개, 2개 + 2개
        # N 5개 사용 : 1개 + 4개, 2개 + 3개
        # N 6개 사용 : 1개 + 5개, 2개 + 4개, 3개 + 3개
        # N 7개 사용 : 1개 + 6개, 2개 + 5개, 3개 + 4개
        # N 8개 사용 : 1개 + 7개, 2개 + 6개, 3개 + 5개, 4개 + 4개
        for part1 in range(1, count // 2 + 1):
            part2 = count - part1
            for num1 in D[part1]: # part1개로 만들 수 있는 수들 탐색
                for num2 in D[part2]: # part2개로 만들 수 있는 수들 탐색
                    # number 만들 수 있으면 return
                    if (
                        num1 + num2 == number or num1 - num2 == number or num2 - num1 == number or
                        num1 * num2 == number or num1 // num2 == number or num2 // num1 == number
                        ):
                        return count

                    # 덧셈 연산
                    D[count].add(num1 + num2)
                    # 뺄셈 연산
                    if num1 - num2 > 0:
                        D[count].add(num1 - num2)
                    if num2 - num1 > 0:
                        D[count].add(num2 - num1)
                    # 곱셈 연산
                    D[count].add(num1 * num2)
                    # 나눗셈 연산
                    if num1 / num2 == num1 // num2:
                        D[count].add(num1 // num2)
                    if num2 / num1 == num2 // num1:
                        D[count].add(num2 // num1)

    return -1


N = 5
number = 5
print(solution(N, number), 1)