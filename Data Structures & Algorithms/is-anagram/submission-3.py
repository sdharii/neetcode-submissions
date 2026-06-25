class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Input: 2 strings (s, t)
        Output: bool -> true if the strings are anagrams of eachother, otherwise false
        Constraints: both strings are lowercase letters
        Edge Cases: 
            if len of strings are different -> return false

        1. determine if the length of both strings are equal
            if they're different, return False
        2. sort both strings using sorted and compare
        """

        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)