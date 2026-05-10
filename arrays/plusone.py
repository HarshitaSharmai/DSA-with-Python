#Leetcode 66 Plusone at last digit
class Solution:
    def plusOne(self,digit):
        for i in range (len(digit),-1,-1,-1):
            if digit[i] < 9:
                digit[i] += 1
            else:
                digit[i] = 0
            i+1
            return digit