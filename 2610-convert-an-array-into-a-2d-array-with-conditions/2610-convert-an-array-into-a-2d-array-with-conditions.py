class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Weekly Contest 339
        n = len(nums)
        c = [0] * (n + 1)
        for i in range(n):
            c[nums[i]] += 1
        res = []
        m = max(c)
        while m > 0:
            if m in c:
                level = []
                for i in range(1, n + 1):
                    if c[i] == m:
                        level.append(i)
                        c[i] -= 1
                res.append(level)
            m -= 1
        return res