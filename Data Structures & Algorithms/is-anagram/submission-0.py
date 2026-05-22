class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sl = []
            tl = []
            for i in sorted(s):
                sl.append(i)
            for i in sorted(t):
                tl.append(i)
            if sl == tl:
                return True
            else:
                return False
        else:
            return False