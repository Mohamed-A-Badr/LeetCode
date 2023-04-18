class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                string += c.lower()
        for i in range(int(len(string) / 2)):
            if string[i] != string[-1 * (i + 1)]:
                return False
        return True

        