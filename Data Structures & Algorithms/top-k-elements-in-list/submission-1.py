class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        I: array of integers, an integer (k)
        O: Return k integers that appear the most in the array
        C: 
        E: 

        1. lets use a freq map (key being the int, value the frequency)
        2. iterate through the array
            if num not in freq map, create an entry
            if num in freq map, + 1
        3. sort freq map in descending order -> we can use labmda expression
        4. for the range of k
            result appends the key of sortedmap[i]
        5. return result
        """

        freqMap = {}

        for value in nums:
            if value not in freqMap:
                freqMap[value] = 1
            freqMap[value] += 1
        
        sortedMap = sorted(freqMap.items(), key = lambda x:x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sortedMap[i][0])

        return result