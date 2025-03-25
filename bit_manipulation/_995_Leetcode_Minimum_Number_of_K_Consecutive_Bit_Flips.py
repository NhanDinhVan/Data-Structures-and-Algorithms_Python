class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # ans = 0

        # for i in range(len(nums) - k + 1):
        #     if(nums[i] == 0):
        #         ans += 1
        #         for j in range(i, i + k):
        #             nums[j] = abs(nums[j] - 1)
        
        # for i in nums:
        #     if(i == 0): return -1
        
        # return ans

        ans = 0
        flipMaker = [0]*(len(nums)+1)
        flipCount = 0

        for i in range(len(nums)):
            flipCount += flipMaker[i]
            if(flipCount%2 == nums[i]):
                if(i+k > len(nums)): return -1
                ans += 1
                flipCount += 1
                flipMaker[i + k] -= 1            

        return ans