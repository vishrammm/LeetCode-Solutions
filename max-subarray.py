class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0 
        max_sum = sum(nums)
       
        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum , current_sum)
            
        return max_sum