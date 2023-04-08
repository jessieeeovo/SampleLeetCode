class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        for i in range(len(nums2)):
            d[nums2[i]] = i
        return [d[n] for n in nums1]