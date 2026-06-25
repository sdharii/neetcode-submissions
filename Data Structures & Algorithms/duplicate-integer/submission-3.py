class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # Edge cases
        if not nums:
            return False

        # Implementation
        for val in nums:
            if val in seen:
                return True
            else:
                seen.add(val)
        return False