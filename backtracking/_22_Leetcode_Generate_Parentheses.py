from typing import List


class Solution:
    def generateParenthesis(self, n):

        result = []

        def backTrack(paren, leftCount, rightCount):

            if leftCount > n: return

            if rightCount > leftCount: return

            if leftCount == rightCount == n:
                result.append(paren)
                return

            backTrack(paren + "(", leftCount + 1, rightCount)
            backTrack(paren + ")", leftCount, rightCount + 1)

        backTrack("", 0, 0)
        return result

