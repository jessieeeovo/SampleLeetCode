class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Weekly Contest 337, 03/19/2023
        count = [0] * value
        for n in nums:
            count[n % value] += 1
        m = min(count)
        res = m * value
        for c in count:
            if c > m:
                res += 1
            else:
                break
        return res
                