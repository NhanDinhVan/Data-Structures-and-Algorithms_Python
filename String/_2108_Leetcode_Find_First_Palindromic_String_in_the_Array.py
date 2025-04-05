class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            l = 0
            r = len(s) - 1
            c = True
            while l < r:
                if s[l] != s[r]:
                    c = False
                    break
                l+=1
                r-=1
            if c:
                return s
        
        return ""