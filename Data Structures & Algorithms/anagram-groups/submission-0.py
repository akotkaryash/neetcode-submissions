from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)

        for s in strs:
            result_dict[''.join(sorted(s))].append(s)
        
        return [x for x in result_dict.values()]