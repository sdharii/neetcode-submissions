class Solution:

    def encode(self, strs: List[str]) -> str:
       "We can add hashtags inbetween and combine it into one string" 
       encoded = ""

       for s in strs:
        encoded += str(len(s)) + "#" + s
       return encoded

    def decode(self, s: str) -> List[str]:
        "perhaps we can split the one string by its hashtags"

        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            word = s[start:end]
            decoded.append(word)

            i = end
        return decoded

