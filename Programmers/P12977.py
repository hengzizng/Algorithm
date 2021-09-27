def solution(nums):
    def combination(index, count, selected): # 3개의 숫자 조합을 구하는 재귀 함수
        if count == 3:
            num = 0
            for i in range(len(selected)):
                if selected[i]:
                    num += nums[i]

            if is_prime[num]:
                answer[0] += 1
            return
        
        if index == len(selected):
            return
        
        selected[index] = True
        combination(index + 1, count + 1, selected)
        selected[index] = False
        combination(index + 1, count, selected)


    # 만들 수 있는 가장 큰 값을 구해서 그 수까지 소수인지를 미리 체크해둔다.
    nums.sort()
    max_num = sum(nums[-3:])
    is_prime = [True] * (max_num + 1)
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, max_num + 1, i):
                is_prime[j] = False

    answer = [0]
    combination(0, 0, [False] * len(nums))

    return answer[0]


nums = [1,2,3,4]
print(solution(nums), 1)
