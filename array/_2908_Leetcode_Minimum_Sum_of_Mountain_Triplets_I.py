class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans = 150
        n = len(nums)

        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        ans = min(ans, nums[i]+nums[j]+nums[k])
        
        return -1 if ans == 150 else ans