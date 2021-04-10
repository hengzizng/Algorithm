# Solution 1 : stack 사용
from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = deque([[]])
        answer = []
        
        while stack:
            permutation = stack.pop()
            
            if len(permutation) < len(nums):
                for num in nums:
                    if num not in permutation:
                        stack.append(permutation + [num])
            else:
                answer.append(permutation)
            
        return answer

# Solution 2 : 재귀 사용
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(permutation):
            if len(permutation) >= len(nums):
                answer.append(permutation)
                return
            for num in nums:
                if num not in permutation:
                    dfs(permutation + [num])
            
        answer = []
        dfs([])
        
        return answer