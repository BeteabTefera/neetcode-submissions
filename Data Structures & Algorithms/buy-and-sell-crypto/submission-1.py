class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Understand:
            - given: Integer array
                    - where prices [i] is the price of said coin on the ith day 
                    - example = prices[20] = 109 is the 20th day 
            - Must buy a single day to buy one coin and another day in the future to sell
            - the days need to be different, meaning the indexe's
            - output:
                    - returning max profit can achieve 
                        - meaning say prices[1] = 10 and sell at prices[3] = 20
                        profit is 10 making it max
                    - base case may choose to not make any transaction;s 
                        profit is 0"
        profit = [] #O(1) space
        length = len(prices) #O(1) runtime due to array's already dictating 

        for i in range(length): #O(N)
            if i == (length - 1):
                break
            
            buy = prices[i]
            sell = max(prices[i+1:]) #O(N) runtime

            if buy < sell:
                profit.append(sell - buy)
        
        return 0 if len(profit) == 0 else max(profit)

            evaluate runtime:
                worst case scenario = O(N^2)
            revise:
                - what can i do to make it better:
                - either hashing or sliding window methodology
                - two pointers should make this to O(N)
        '''
        max_profit = 0 
        left = prices[0]

        for i in range(len(prices)-1):
            right = prices[i+1]
            if left < right:
                if (right - left) > max_profit:
                    max_profit = right - left
            else:
                left = right
            print (f"i:{i}, left:{left}, right:{right}, list:{prices}")
        return max_profit



        
        
        