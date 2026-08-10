class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        input: int array (heights) -> each val represents the height of             each bar
        output: int (max amount of water a container can store)
            - looking at area. we ONLY have the heights
        implementation:
            instantiate pointer at the end of heights array
            instantiate a maxAmount variable to keep track of each calculation

            loop through the heights array
                ENSURE heights[i] != heights[pointer] (if then); if it is, break
                determine which pointer is the height (whichever is smallest)
                calculate the distance (pointer - i), WIDTH
                create a temp variable to calculate the area (height x               distance/width)

                if temp > maxAmount, maxAmount = temp

            return maxAmount
        """

        # pointer = len(heights) - 1
        # maxAmount = 0

        # for i in range(len(heights)):
        #     if i != pointer:
        #         currHeight = min(heights[i], heights[pointer])
        #         width = pointer - i
        #         temp = currHeight * width

        #         if temp > maxAmount:
        #             maxAmount = temp
        # return maxAmount

        # maxAmount = 0

        # for i in range(len(heights)):
        #     pointer = i + 1

        #     while pointer < len(heights):
        #         currHeight = min(heights[i], heights[pointer])
        #         width = pointer - i
        #         temp = currHeight * width

        #         if temp > maxAmount:
        #             maxAmount = temp
        # return maxAmount

        maxAmount = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            currHeight = min(heights[left], heights[right])
            width = right - left
            temp = currHeight * width

            if temp > maxAmount:
                maxAmount = temp
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxAmount
