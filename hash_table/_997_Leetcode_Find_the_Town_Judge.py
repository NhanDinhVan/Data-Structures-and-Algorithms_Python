class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1 

        bi = {} 
        ai = set()  

        for tr in trust:
            bi[tr[1]] = bi.get(tr[1], 0) + 1 
            ai.add(tr[0])  

        for i in range(1, n + 1):
            if i not in ai and bi.get(i, 0) == n - 1:
                return i

        return -1 