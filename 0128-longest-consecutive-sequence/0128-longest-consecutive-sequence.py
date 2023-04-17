class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        st = sorted(list(set(nums)))
        cnt, res = 1, 1
        for i in range(1, len(st)):
            if st[i] - st[i - 1] == 1:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 1
        return res