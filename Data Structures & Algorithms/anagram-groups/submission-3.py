class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        myDict = defaultdict(list)

        """
        loop through strs, sort word, add to dict keysif not in there.
        if word already in dict, add it to values
        loop through dict values and append res
        """

        for word in strs:
            sortedWord = "".join(sorted(word))  
            # add to dictionery
            if sortedWord in myDict:
                myDict[sortedWord].append(word)
            else:
                myDict[sortedWord].append(word)
        
        for value in myDict.values():
            res.append(value)
        return res