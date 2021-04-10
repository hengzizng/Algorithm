# Solution 1 >
from collections import deque

class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs():
            stack = deque([''])
            answer = []
            
            while stack:
                letters = stack.pop()
                if len(letters) < len(digits):
                    for char in chars[digits[len(letters)]]:
                        stack.append(letters + char)
                else:
                    answer.append(letters)
            return answer
                    
        
        if not digits:
            return []
                    
        chars = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        return dfs()


# Solution 2
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, string):  # index : digits에서 현재 인덱스 / string : 현재 만드는중인 문자열
            # 문자열이 만들어져야하는 길이만큼 만들어졌으면 종료
            if len(string) == len(digits):
                answer.append(string)
                return
            
            for char in dic[digits[index]]:
                dfs(index + 1, string + char)
            
        # digits가 빈 문자열일 때 예외처리
        if not digits:
            return digits
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []
        
        dfs(0, "")
        return answer