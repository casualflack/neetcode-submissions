class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram in hash_map:
                hash_map[anagram].append(s)
            else:
                hash_map[anagram] = [s]
        
        res = []
        for key in hash_map:
            res.append(hash_map[key])
        
        return res