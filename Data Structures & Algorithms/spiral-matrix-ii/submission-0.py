class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left = 0
        right = n
        top = 0
        bottom = n

        count = 1 # track number that needs to be inputted into the spirl

        while left < right and top < bottom:
            #top row
            for i in range(left,right):
                res[top][i] = count
                count += 1
            top += 1 #top bound @ 1

            #right column
            for i in range(top, bottom):
                res[i][right-1] = count
                count += 1
            right -= 1 #right bount @2

            #bottom row
            for i in range(right-1, left-1, -1):
                res[bottom-1][i] = count
                count += 1
            bottom -= 1 #bottom bound @ 2

            #left column (excluding 1)
            for i in range(bottom-1,top-1, -1):
                res[i][top-1] = count
                count += 1
            left += 1 #left bound @ 1
        return res
