# Submission 1
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        max_len, start, end = 0, 0, 0
        
        while end < len(s):
            if s[end] not in used:
                used.add(s[end])
                end += 1
            else:
                max_len = max(max_len, len(used))
                used.remove(s[start])
                start += 1
        
        return max(max_len, len(used))

# Submission 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
        
            used[char] = index
                
        return max_length