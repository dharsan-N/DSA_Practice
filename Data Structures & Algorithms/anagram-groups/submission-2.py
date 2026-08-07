from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for x in strs:
            ss="".join(sorted(x))
            dic[ss].append(x)
        return list(dic.values())