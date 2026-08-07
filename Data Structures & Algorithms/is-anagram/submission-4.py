from string import printable
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s)==set(t) and len(s)==len(t) and all(s.count(i)==t.count(i) for i in set(s)):
            return True
        return False
        