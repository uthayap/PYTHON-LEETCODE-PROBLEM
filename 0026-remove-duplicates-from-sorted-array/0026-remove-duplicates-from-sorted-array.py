class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
        
        # Modify the original list in-place
        nums[:] = unique
        return len(nums)