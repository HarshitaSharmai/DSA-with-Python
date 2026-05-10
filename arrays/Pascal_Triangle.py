#Leetcode 118 Pascal Triangle
class Solution:
    
    def pascal(self,numrows:int) -> list[list[int]]:
        triangle = []
        for i in range (numrows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
    
n = int(input("Enter number of rows: "))
obj = Solution()
print(obj.pascal(n))