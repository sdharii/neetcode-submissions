class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        U
            I: str (s), str (t)
            O: bool -> true if the strings are anagrams, otherwise false
            C: s and t consist of lowercase letters
            E: 
                both empty string(s) -> return true
                different lengths -> return false
        P
            create edge cases

            create two dictionaries for each str
            iterate through the len(s)
                append each letter to dict, increase the times its seen if valid
                repeat with string t
            return {} == {}
        """
        if s and t == " ":
            return True
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) 
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT