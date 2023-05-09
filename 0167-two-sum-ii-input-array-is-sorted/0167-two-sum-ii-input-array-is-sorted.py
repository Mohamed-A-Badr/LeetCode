class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers) - 1
        while l < r :
            sm = numbers[l] + numbers[r]
            if sm == target:
                res.append(l + 1)
                res.append(r + 1)
                return res
            elif sm < target:
                l += 1
            else:
                r -= 1
        