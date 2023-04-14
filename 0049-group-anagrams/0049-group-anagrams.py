from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = defaultdict(list)
        for s in strs:
            st = "".join(sorted(s))
            mp[st].append(s)
        for k, v in mp.items():
            res.append(v)
        return res
        
                