class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            temp = 0
            for j in i:
                temp += j

                if(max_wealth < temp):
                    max_wealth = temp
        return max_wealth
                    
