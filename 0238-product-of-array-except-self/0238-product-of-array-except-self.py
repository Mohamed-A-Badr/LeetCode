class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cntz = 0
        pro = 1 
        for i in nums:
            if i == 0:
                cntz += 1
                continue
            pro *= i
        res =[]
        for i in nums:
            if cntz > 1:
                res.append(0)
            elif cntz == 1:
                res.append(int(pro) if i == 0 else 0)
            else: 
                res.append(int(pro/i))
                
        return res
        