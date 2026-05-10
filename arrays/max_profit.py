
#Leetcode 121 To find max profit by buy and selling of stocks
import platform
class Solution2:
    def maxProfit(self,prices:list[int]) -> int:
        max_profit = 0
        for i in range (len(prices)):
            for j in range (i+1,len(prices)):
                profit = prices[j]-prices[i]
                max_profit = max(profit,max_profit) 
        return max_profit
        
prices = list(map(int,input("Enter prices of each day:").split()))
obj = Solution2()
print(obj.maxProfit(prices))