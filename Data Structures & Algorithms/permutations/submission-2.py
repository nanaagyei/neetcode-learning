class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perm = []
            for p in perms:
                for i in range(len(p) + 1):
                    new_perm.append(p[:i] + [n] + p[i:])
            perms = new_perm
        return perms
