class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        I: array of strings
        O: 2D array of grouped anagrams
        C: all strings are made up of lowercase letters
        E: 
            Empty array -> return 2D array with "" ex: [[""]]
            Only 1 string -> Return 2D array with str ex: [["x"]]
        
        1. implement a dictionary where keys are the sorted strings, values are the original words
        2. iterate through strings and sort them using sorted().
            if sortedword not in dict -> add an entry
            else add to current entry if in dict
        3. create empty list
        4. iterate through all dict keys
            append all dict.keys in empty list, but inside another list (nested)
        """
        
        myDict = {}

        for string in strs:
            sortedString = "".join(sorted(string))

            if sortedString not in myDict:
                myDict[sortedString] = []
            myDict[sortedString].append(string)

        return list(myDict.values())
        
        