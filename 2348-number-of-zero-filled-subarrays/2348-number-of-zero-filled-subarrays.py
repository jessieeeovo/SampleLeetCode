class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counts = []
        c = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                if c != 0:
                    counts.append(c)
                    c = 0
            else:
                c += 1
        if c != 0:
            counts.append(c)
        return sum([x*(x+1)//2 for x in counts])