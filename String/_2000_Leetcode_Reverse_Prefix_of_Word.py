class Solution:
    def reversePrefix(self, word: str, ch: str) -> str: 
        w = list(word)
        for i in range(len(w)):
            if w[i] == ch:
                l = 0
                r = i
                while l < r:
                    tmp = w[l]
                    w[l] = w[r]
                    w[r] = tmp
                    l += 1
                    r -= 1
                break
        return "".join(w)