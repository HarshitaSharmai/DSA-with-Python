#Leetcode 27 Remove given value
class Solution:
    num = [3,2,2,3]
    val = 3
    def removeval(self,num):
        n = len(num)
        for i in range (num):
            if i != val:
            return num[i] == num[i+1]
        else:
            i = i+1
        
            