class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        ans = strs[0]

        for s in strs:
            while not s.startswith(ans):
                ans = ans[:-1]
                if ans == "" : return ""
        return ans
        