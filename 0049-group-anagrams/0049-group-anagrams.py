from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            st = "".join(sorted(s))
            mp[st].append(s)
        
        return mp.values()
        
                