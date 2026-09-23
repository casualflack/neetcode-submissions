class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0 
        right = 0
        seen = set()
        
        while right < len(s):
            if s[right] not in seen:
                length = right - left + 1
                longest = max(longest, length)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            
            seen.add(s[right])
            right += 1
        
        return longest