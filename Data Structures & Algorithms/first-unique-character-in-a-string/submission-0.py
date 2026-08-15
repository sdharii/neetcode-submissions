class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        countDict = Counter(s)

        for i, c in enumerate(s):
            if countDict[c] == 1:
                return i
        return -1