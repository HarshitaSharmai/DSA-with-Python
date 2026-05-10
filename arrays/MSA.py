#Leetcode 53 MAXSUBARRAY
class Solution:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    def maxsubarray(self,nums):
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range (1, len(nums)):
            current_sum = max(nums[1],current_sum+nums[i])
            max_sum = max(max_sum,current_sum)
        return(print(max_sum))