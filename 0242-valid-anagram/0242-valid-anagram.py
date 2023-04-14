class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st1 = "".join(sorted(s))
        st2 = "".join(sorted(t))
        return st1 == st2