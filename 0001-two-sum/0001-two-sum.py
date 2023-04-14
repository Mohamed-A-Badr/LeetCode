from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for idx, x in enumerate(nums):
            if x in mp:
                return [idx, mp[x]]
            else:
                mp[target-x] = idx
                