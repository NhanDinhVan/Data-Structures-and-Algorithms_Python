class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr = [0]*501

        for n in nums:
            arr[n] += 1
        
        for i in range(501):
            if(arr[i] != 0 and arr[i]%2 != 0): return False

        return True



        