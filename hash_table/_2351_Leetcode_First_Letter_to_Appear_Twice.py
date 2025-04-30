class Solution:
    def repeatedCharacter(self, s: str) -> str:
        myset = set()
        for i in range(len(s)):
            if s[i] in myset:
                return s[i]
            myset.add(s[i])
        return 'c'