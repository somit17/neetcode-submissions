class Solution:
    def climbStairs(self, n: int) -> int:
        #Two approaches
        #Top-Down
        #Using Memoisation
        memo = {}
        def top_down_approach(n) -> int:
            if n in memo:
                return memo[n]
            
            if n == 1 : return 1
            if n == 2 : return 2

            result = top_down_approach(n-1)+top_down_approach(n-2)
            memo[n] = result
            return result

        return top_down_approach(n)