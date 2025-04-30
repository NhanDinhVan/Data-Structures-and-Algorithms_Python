class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sg = 0
        db = 0
        for n in nums:
            if n > 9 : db += n
            else : sg += n
        return sg!=db