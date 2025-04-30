class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        idx =-1
        ans = 0

        while idx < len(nums):
            seen = set()
            check = True
            for i in range(idx + 1, len(nums)):
                if nums[i] in seen:
                    check = False
                    break
                seen.add(nums[i])
            if check: return ans
            ans += 1
            idx += 3
        return ans