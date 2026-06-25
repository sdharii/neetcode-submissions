class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base Case
        if (not s and not t):
            return True
        if len(s) != len(t):
            return False
        
        # Implementation
        sHashMap = Counter(s)
        tHashMap = Counter(t)

        if (sHashMap == tHashMap):
            return True
        return False