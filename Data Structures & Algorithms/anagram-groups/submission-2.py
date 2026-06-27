class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        result = []

        # Edge Cases
        if len(strs) == 1:
            result.append(strs)
            return result
        if not strs:
            return result

        # Implementation
        for i in strs:
            sortedVer = ''.join(sorted(i))
            if sortedVer in myDict:
                myDict[sortedVer].append(i) # Adding onto the list of values
            else:
                myDict[sortedVer] = [i] # Creates a new key

        result = list(myDict.values())
        return result