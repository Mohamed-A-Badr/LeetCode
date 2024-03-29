class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 0
        dct = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
        res = list(dct.keys())[:k]
        return res