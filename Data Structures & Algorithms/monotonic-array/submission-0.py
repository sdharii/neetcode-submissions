class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        input: int array (nums)
        output: bool -> true if monotonic, false otherwise
        implementation:
            instanstiate 2 vars, decreasing & increasing (bools)
            loop through nums (i) -- start range at 1
                check if the array is decreasing
                    if nums[i] > nums[i-1]:
                        decreasing = true
                    
                check if array is increasing:
                    if nums[i] < nums[i-1]:
                        increasing = true
            
            if decreasing or increasing == true, return true
                             
        """
        increase = True

        for i in range (1, len(nums)):
            if nums[i] < nums[i-1]:
                increase = False
                break
            
        if increase:
            return True

        decrease = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decrease = False
                break
        
        return decrease
        