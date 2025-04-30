class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        idx = 0
        while n > 0:
            cur = n & 1
            if cur == 1 : 
                ans[idx % 2] += 1
            idx += 1
            n >>= 1
        return ans