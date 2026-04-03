class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = right

        while left <= right:

            mid = (left + right) // 2 # rate k
            total = 0

            for pile in piles:
                total += math.ceil(pile/mid)
            
            if total <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return k

