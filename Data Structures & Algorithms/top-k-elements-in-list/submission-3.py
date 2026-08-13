class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        res = []

        for num in nums:
            countNums[num] = 1 + countNums.get(num, 0)
        
        countNums = dict(sorted(countNums.items(), key=lambda item: item[1], reverse=True))

        freq = list(countNums.keys())[:k]

        return freq

