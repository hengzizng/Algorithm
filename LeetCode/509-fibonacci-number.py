from collections import defaultdict
import pprint


pp = pprint.PrettyPrinter(indent=4)

# 풀이 1 > 재귀 구조 브루트 포스
def fibonacci_number_1(N: int) -> int:
    print(N)
    if N <= 1:
        return N
    return fibonacci_number_1(N-1) + fibonacci_number_1(N-2)

# 풀이 2 > 메모이제이션(하향식)
class Solution2:
    dp = defaultdict(int)

    def fibonacci_number_2(self, N: int) -> int:
        print(N)
        if N <= 1:
            return N
        
        if self.dp[N]:
            return self.dp[N]

        self.dp[N] = self.fibonacci_number_2(N-1) + self.fibonacci_number_2(N-2)
        return self.dp[N]

# 풀이 3 > 타뷸레이션(상향식)
class Solution3:
    dp = defaultdict(int)
    def fibonacci_number_3(self, N: int) -> int:
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[N]

# 풀이 4 > 풀이 3에서 두 변수만 이용해 공간 절약
def fibonacci_number_4(N: int) -> int:
    x, y = 0, 1
    for i in range(N-1):
        x, y = y, x + y
        print(y)
    
    return y


num = 10

# answer = fibonacci_number_1(num)

# solution = Solution2()
# answer = solution.fibonacci_number_2(num)

# solution = Solution3()
# answer = solution.fibonacci_number_3(num)

answer = fibonacci_number_4(num)

print(answer)