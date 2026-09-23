class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = float('inf')
        for num in nums:
            smallest = min(smallest, num)
        return smallest
