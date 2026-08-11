class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        input: int array (nums)
        output: int (length of the longest consecutive sequence)
        constraints: must run in O(n) time
        implementation:
            use a set to keep lookup O(1)
            loop through nums
                if num-1 not in set it's the start of a sequence

                
        """
        mySet = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in mySet:
                length = 1

                while (num + length) in mySet:
                    length += 1
                
                longest = max(length, longest)
        return longest



