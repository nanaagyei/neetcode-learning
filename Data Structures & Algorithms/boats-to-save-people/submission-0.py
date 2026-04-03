class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        minBoats = 0

        while left <= right:
            remaining = limit - people[right]
            minBoats += 1
            right -= 1

            if left <= right and remaining >= people[left]:
                left += 1
        
        return minBoats

