class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        bit_mask = 0
        maxL = 0

        for r in range(len(nums)):
            while(nums[r] & bit_mask != 0):
                bit_mask ^= nums[l]
                l += 1
            
            bit_mask |= nums[r]
            maxL = max(maxL, r - l + 1)

        return maxL