class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = Counter(nums)

        # Implementation
        return [num for num, freq in freqMap.most_common(k)]