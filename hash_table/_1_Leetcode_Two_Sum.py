class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}

        for i, num in enumerate(nums):
            n = target - num
            if n in map_dict:
                return [map_dict[n], i]
            map_dict[num] = i

        return []