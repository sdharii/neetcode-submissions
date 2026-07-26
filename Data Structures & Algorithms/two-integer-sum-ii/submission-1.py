class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        input: int array (numbers); sorted in ascending order, int (target)
        output: list of 2 indices, must add up to the target
        constraints:
            # indices start @ 1!!
            # index1 < index 2 & index1 + index2 = target
            # there's always ONE valid solution
            # must be O(1) additional space
        implementation:
            for loop through numbers (consider that pointer1)
                pointer2 = pointer1 + 1 (starts it at the number next to pointer 1 each iteration)
                while pointer2 < length of numbers (keeps it in range)
                    check if pointer1 + pointer2 = target
                        if true, return [pointer1 + 1, pointer2 + 1]
                    if not true, pointer2 += 1          
        """

        for number in range(len(numbers)):
            rPointer = number + 1

            while rPointer < len(numbers):
                if numbers[number] + numbers[rPointer] == target:
                    return [number+1, rPointer+1]
                rPointer +=1
