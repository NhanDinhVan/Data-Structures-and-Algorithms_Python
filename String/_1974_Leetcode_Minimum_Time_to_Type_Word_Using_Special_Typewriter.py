class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        p = 'a'

        for i in range(len(word)):
            ans += min(26 - abs(ord(p) - ord(word[i])), abs(ord(p) - ord(word[i]))) + 1
            p = word[i]
        return ans
