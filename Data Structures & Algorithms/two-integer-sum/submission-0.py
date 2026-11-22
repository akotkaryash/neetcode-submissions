from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict()

        for i, val in enumerate(nums):
            if (target - val) in indexes:
                return [indexes[target - val], i]
            indexes[val] = i

        return []