class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = set(nums)

        result = 0

        for num in nums:
            if (num-1) not in present:
                count = 1
                n = num + 1
                while n in present:
                    count += 1
                    n += 1
                result = max(result, count)

        return result

        