class Solution:
    def isPalindrome(self, num: int) -> bool:
        s = [x for x in str(num)]
        rev = s.copy()[::-1]
        return s == rev
        