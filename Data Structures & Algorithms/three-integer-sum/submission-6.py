class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        input: int array (nums)
        output: a list of ints -> 3 elements that add up to == 0
        edge cases/constraints: 
            - output shouldn't contain any duplicate triplets
            - all indices must be distinct
        implementation:
            - instantiate a result variable, which is a list
            - loop through nums
                - nested loop through nums as second pointer
                    - create pointer @ j + 1
                    - if nums[i] + nums[j] + nums[k] == 0 add to result
            - return result
        """

        # Decided to brute force it for now, will figure out a O(n^2) algorithm next time; It actually won't let me submit it...
        
        # result = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range (j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i],nums[j],nums[k]]
        #                 result.add(tuple(temp))
        # return [list(i) for i in result]

        result = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
                