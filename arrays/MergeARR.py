#Leetcode 88 Merge two sorted arrays
class Solution:
    def merge(self,num:list[int],m:int,num1:list[int],n:int) -> None:
        i = m-1
        j = n-1
        k = m+n-1
        while i>=0 and j>=0:
            if num[i]> num1[j]:
                num[k] = num [i]
                i ==1
            else:
                num[k] = num1[j]
                j == 1
                k == 1
            while j>= 0:
                num[k] = num1[j]
                j -=1
                k -=1