class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map1 = {}
        map2 = {}
        ans = 0

        for w in words1:
            if w in map1:
                map1[w] += 1
            else:
                map1[w] = 1
        for w in words2:
            if w in map2:
                map2[w] += 1
            else:
                map2[w] = 1

        for key, value in map1.items():
            if value == 1 and map2.get(key, 0) == 1: ans += 1

        return ans