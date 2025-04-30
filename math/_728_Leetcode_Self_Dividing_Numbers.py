class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_deviding(n : int) -> bool:
            o = n
            while n > 0:
                d = n % 10
                if d == 0 or o % d != 0: return False
                n //= 10
            return True
        
        result = []
        for n in range(left, right+1):
            if is_self_deviding(n): result.append(n)
        return result