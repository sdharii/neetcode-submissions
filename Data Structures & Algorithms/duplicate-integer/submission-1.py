class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        
        seen = set()
    
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        ''''
        U
            I: int array (nums)
            O: bool -> true if there is a duplicate, otherwise false
            C: n/a
            E: 
                empty array -> return false
        P
            if nums == []
                return false
            create a hashset to keep track of unique ints
            iterate through nums
                if num not in hashset
                    append to hashset
                else if num in hashset
                    return true
            otherwise return false
        '''
        