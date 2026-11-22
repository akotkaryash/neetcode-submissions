from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = [[val, x] for x, val in Counter(nums).items()]
        heapq.heapify_max(h)
        return [heapq.heappop_max(h)[1] for i in range(k)]

        