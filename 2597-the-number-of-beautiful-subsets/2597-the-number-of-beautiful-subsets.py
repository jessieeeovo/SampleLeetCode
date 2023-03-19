class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Weekly Contest 337, 03/19/2023
        def backtrack(first=0, curr=[]):
            res = 0
            for i in range(first, n):
                if nums[i] + k not in curr and nums[i] - k not in curr:
                    curr.append(nums[i])
                    res += 1 + backtrack(i + 1, curr)
                    curr.pop(-1)
            return res
        n = len(nums)
        return backtrack()