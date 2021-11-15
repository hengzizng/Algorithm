from collections import deque


def solution(expression):
    #
    def calc(opers_priority, opers, nums):
        for oper_priority in opers_priority: # 연산자 우선순위순으로 반복
            count = len(opers)
            while count > 0: # 수식 내에 있는 연산자 반복                
                opers.append(opers.popleft())
                nums.append(nums.popleft())
                
                if opers[-1] == oper_priority:
                    num1 = nums.pop()
                    num2 = nums.popleft()
                    oper = opers.pop()
                    if oper == '+':
                        nums.appendleft(num1 + num2)
                    elif oper == '-':
                        nums.appendleft(num1 - num2)
                    else:
                        nums.appendleft(num1 * num2)
                count -= 1
            nums.append(nums.popleft()) # 숫자가 연산자보다 하나 많기 때문에 마지막 남은 하나를 맨 뒤로 보내준다
        max_value[0] = max(max_value[0], abs(int(nums.pop())))
                    
    
    # 연산자 우선순위 순열
    def get_oper_perm(count, selected, oper_perm):
        if count == len(opers_list):
            copy_opers = copy(opers)
            copy_nums = copy(nums)
            calc(oper_perm, copy_opers, copy_nums)
            return
        
        for i in range(len(opers_list)):
            if not selected[i]:
                oper_perm[count] = opers_list[i]
                selected[i] = True
                get_oper_perm(count + 1, selected, oper_perm)
                selected[i] = False
    
    # 큐 복사
    def copy(origin):
        copied = deque()
        
        for element in origin:
            copied.append(element)
            
        return copied
    
    
    # 숫자들과 연산자들로 분리
    opers, nums = deque(), deque()
    opers_list = set()
    num = ""
    for char in expression:
        if '0' <= char <= '9':
            num += char
        else:
            nums.append(int(num))
            num = ""
            opers.append(char)
            opers_list.add(char)
    nums.append(int(num))
    opers_list = list(opers_list)
    
    
    max_value = [0]
    get_oper_perm(0, [False] * len(opers_list), [''] * len(opers_list))
    
    return max_value[0]