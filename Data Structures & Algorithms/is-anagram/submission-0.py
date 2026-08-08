from string import printable


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if all(s.count(i) == t.count(i) for i in set(s)):
                return True
        return False
