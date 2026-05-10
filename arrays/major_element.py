#Leetcode 169 To find the major element in a list
#The major element is the element that appears more than n/2 times in the list
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
element = list(map(int, input("Enter number of elements:").split()))
obj = Solution()
print(obj.majorityElement(element))