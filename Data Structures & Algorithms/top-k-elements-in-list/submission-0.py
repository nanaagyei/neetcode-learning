class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elems_hash = {}

        for num in nums:
            freq_elems_hash[num] = 1 + freq_elems_hash.get(num, 0)
        
        freq_elems_hash = dict(sorted(freq_elems_hash.items(), key=lambda item: item[1], reverse=True))

        return list(freq_elems_hash.keys())[:k]