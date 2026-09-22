class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        leftproduct = 1

        for i in range(len(nums)):
            ans[i] = leftproduct
            leftproduct = leftproduct * nums[i]
        
        rightproduct = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * rightproduct
            rightproduct = rightproduct * nums[i]
        
        return ans

        