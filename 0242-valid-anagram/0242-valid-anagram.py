class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in s:
            if ch not in t:
                return False
            t = t.replace(ch,'',1)
        return t == ''
        