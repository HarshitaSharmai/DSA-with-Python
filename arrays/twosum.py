#Leetcode 1st TWOSUM problem
class twosum:
    nums = [1,2,3,4,5,6]
    target = 9
    def sum(self,nums):
        n = len(nums)
        for i in range(n):
            for j in range (i+1, n):
                if i+j == target:
                    return [i,j]
                    print [i,j]