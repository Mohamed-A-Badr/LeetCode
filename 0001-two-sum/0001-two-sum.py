from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(list)
        idx = 0
        for idx, x in enumerate(nums):
            mp[x].append(idx)

        for idx, i in enumerate(nums):
            x = target - i
            for j in mp[x]:
                if j == idx:
                    continue
                return [idx, j]