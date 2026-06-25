class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        U
            I: string array (str)
            O: return a list of sublists (group all anagrams tgt)
            C: strs[i] is lowercase letters
            E: 
        P 
            create a anagram list to keep track of the sublists
            iterate through str, for i in len(range(str))
                for j in range(i+1)
                    if (len(j) == len(i)) and (sorted(j) == sorted(i))
                        anagrams.append([str[i],str[j]])
        """
        myDict = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            myDict[key].append(word)
        return list(myDict.values())

