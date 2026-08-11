class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        input: int array (nums), int (target)
        output: a list of indices (i & j)
        constraints:
            - nums[i] + nums[j] must equal target
            - i cannot equal j
            - only ONE valid answer exists
        edge cases: 
        implementation:
            instanstiate a hashmap (key = num, val = index)
            loop through nums using enumerate (i,n)
                determine complement (target - nums[i])
                if complement in hashmap 
                    return [i, hashmap[complement]]
                else hashmap[n] = i (add it to hashmap)
                
        """
        myMap = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in myMap:
                return [myMap[complement], i]
            myMap[n] = i
