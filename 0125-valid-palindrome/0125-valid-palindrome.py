class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(ch for ch in s if ch.isalnum()).lower()
        return string == string[::-1]

        