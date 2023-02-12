class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # weekly contest 2/11/2023
        def binarySearchForLower(target, left):
            right = n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binarySearchForUpper(target, left):
            right = n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        res = 0
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 1):
            lowerBound = binarySearchForLower(lower - nums[i], i + 1)
            upperBound = binarySearchForUpper(upper - nums[i], i + 1)
            res += upperBound - lowerBound
        return res