class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for integer in nums:
            if integer in seen:
                return True
            seen.add(integer)
        return False
        