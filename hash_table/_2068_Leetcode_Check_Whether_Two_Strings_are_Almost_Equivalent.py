class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        for c in set(freq1.keys()).union(freq2.keys()):  
            if abs(freq1.get(c, 0) - freq2.get(c, 0)) > 3:
                return False

        return True