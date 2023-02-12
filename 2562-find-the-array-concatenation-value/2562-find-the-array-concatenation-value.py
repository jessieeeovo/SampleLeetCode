class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        # weekly contest 2/11/2023
        def recursive_helper(nums, conc):
            if not nums:
                return conc
            if len(nums) == 1:
                return nums[0] + conc
            return int(str(nums[0]) + str(nums[-1])) + recursive_helper(nums[1:-1], conc)
        
        return recursive_helper(nums, 0)