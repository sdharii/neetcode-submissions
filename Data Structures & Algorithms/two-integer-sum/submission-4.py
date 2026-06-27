class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        sub = 0 # target - i

        for i in range(len(nums)):
            sub = target - nums[i]
            for j in range(i):
                if (nums[j] == sub):
                    result.append(j)
                    result.append(i)
        return result

