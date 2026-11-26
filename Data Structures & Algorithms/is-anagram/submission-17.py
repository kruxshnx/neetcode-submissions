class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sort()
        if len(s)!= len(t):
            return False
        return True

        