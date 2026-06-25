class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Input: int array (nums)
        Output: bool -> true if any val appears more than once, otherwise false
        Constraints: N/A
        Edge cases: 
            empty arr -> return false
            arr len(1) -> return false
        
        1. use a set to keep track of nums 
        2. iterate through the array
            if num not in set:
                add to set
            other if num is in set:
                return true
        """

        seen = set()

        for val in nums:
            if val not in seen:
                seen.add(val)
            else:
                return True 
        return False