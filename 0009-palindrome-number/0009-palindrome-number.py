class Solution:
    def isPalindrome(self, num: int) -> bool:
        s = str(num)
        rev = s[::-1]
        return s == rev
        