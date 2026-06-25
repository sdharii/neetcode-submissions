class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U:
            I: int array (nums), int (target)
            O: return the indices of i and j, assuming nums[i] + nums[j] == target and i != j
            C: 
        P
            iterate through nums [i]
                iterate through nums [j] 
                    if nums[i] + nums[j] == target and i != j
                        return [i,j]
                    else continue
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target and i != j:
                    return sorted([i,j])
                continue
        