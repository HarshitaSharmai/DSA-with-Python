#Leetcode 26 Remove duplicate from an array list
class Removeduplicates :
    nums = [0,0,1,1,1,2,2,3,3,4]
    def removeduplicates(self,nums):
        n = len(nums)
        if n == 0:
                return 1
        else:
         for i in range(n):
             for j in range(i+1, n):
                 if i != j:
                     return i == j
                 else:
                     s = nums[j]
        return i+1
    
            
            
            
                