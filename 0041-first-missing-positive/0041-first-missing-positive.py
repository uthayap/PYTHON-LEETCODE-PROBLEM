class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        nums = set(nums)
        
        while i in nums:
            i += 1
        
        return i