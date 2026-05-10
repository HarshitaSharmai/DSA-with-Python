#Leetcode 136 To print a single number in a list
nums = list(map(int,input("Enter multiple number with a single number:").split()))
class Solution:
    def single_num(self,nums:list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
obj = Solution()
print ("Single number is :", (obj.single_num(nums)))
            