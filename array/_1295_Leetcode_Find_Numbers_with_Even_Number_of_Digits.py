class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if num < 10 : continue
            n = num
            count = 0
            while n > 0:
                count += 1
                n = n//10
            if count % 2 == 0 : ans+=1
        return ans