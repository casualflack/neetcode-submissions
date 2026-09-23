from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)
        left = 0

        for c in t: #initialize the need hashmap
            need[c] += 1
        
        have = 0
        required = len(need)
        res = [-1, -1]
        shortest = float('inf')

        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            while have == required and left <= right: #window contains everything we need
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    res = [left, right]
                leftchar = s[left]
                window[leftchar] -= 1
                if leftchar in need and window[leftchar] < need[leftchar]:
                    have -= 1
                left += 1

        start, end = res
        return s[start:end + 1] if shortest != float('inf') else ""