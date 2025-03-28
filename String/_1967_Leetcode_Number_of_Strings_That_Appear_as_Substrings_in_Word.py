class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for i in range(len(patterns)):
            if word.find(patterns[i]) != -1: 
                ans+=1
        return ans