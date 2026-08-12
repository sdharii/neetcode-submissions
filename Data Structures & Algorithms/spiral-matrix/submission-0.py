class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # boundary variables
        topBound = 0
        bottomBound = len(matrix)
        leftBound = 0
        rightBound = len(matrix[0])

        # left < right & top < bottom
        while leftBound < rightBound and topBound < bottomBound:
            # top row
            for i in range(leftBound, rightBound):
                res.append(matrix[topBound][i])
            topBound += 1 #shrinks top boundary

            #last column
            for i in range(topBound, bottomBound):
                res.append(matrix[i][rightBound-1])
            rightBound -= 1

            # check if left > right or top > bottom -> break if so
            if not (leftBound < rightBound and topBound < bottomBound):
                break

            #bottom row
            for i in range(rightBound - 1, leftBound-1, -1):
                res.append(matrix[bottomBound-1][i])
            bottomBound -= 1
            #first column (remember topBound shrunk and we're going bottom to top)
            for i in range(bottomBound-1, topBound-1, -1):
                res.append(matrix[i][leftBound])
            leftBound += 1

        return res


