class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0
        lpointer = 0

        for rpointer in range(len(s)):
            #if char in seen
            while s[rpointer] in seen:
                seen.remove(s[lpointer])
                lpointer += 1
            #if char not in seen
            seen.add(s[rpointer])

            result = max(result, rpointer - lpointer + 1)
        return result
            
