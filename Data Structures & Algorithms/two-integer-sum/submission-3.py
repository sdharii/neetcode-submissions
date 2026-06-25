class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input: 
        Output:
        Constraints:
        Edge Cases:
        """
    
        prevMap = {}

        for i, number in enumerate(nums):
            complement = target - number
            if complement in prevMap:
                return [prevMap[complement], i]
            
            prevMap[number] = i 
                