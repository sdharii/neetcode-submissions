class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = s.replace(" ","").lower()

        pointer1 = 0
        pointer2 = len(cleanedStr)-1

        if not cleanedStr:
            return True

        while pointer1 <= pointer2:
            while pointer1 < pointer2 and not cleanedStr[pointer1].isalnum():
                pointer1 += 1
            
            while pointer1 < pointer2 and not cleanedStr[pointer2].isalnum():
                pointer2 -= 1
                
            if cleanedStr[pointer1] != cleanedStr[pointer2]:
                return False
                
            pointer1 += 1
            pointer2 -= 1
        return True