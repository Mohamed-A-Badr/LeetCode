class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        st = sorted(set(nums))
        cnt, res = 1, 1
        for i in range(1, len(st)):
            if st[i] - st[i - 1] == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
        return res