class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                         ans+=1
        
        return ans