class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U
            I: int array (nums), int (k)
            O: return the top "k" most freq elements within the array
            C: k is greater than or equal to 1 but less than the num of elements in nums
            E: 
                empty list -> return None
                all unique ints -> return None
        P
            create a freqMap using counter
            initialize a greatest variable
            initialize res list
            iterate through freqmap
                if value > greatest
                    greatest = key
   
        """
        if not nums:
            return None

        freqMap = Counter(nums)
        most_common = freqMap.most_common(k)

        return [num for num, count in most_common]
        