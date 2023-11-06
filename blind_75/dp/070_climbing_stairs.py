class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # init dp arr size n + 1, to include base (0) step
        dp = [0] * (n + 1)

        # base cases
        # only one way to get to step 0 (0 steps), step 1 (1 step)
        dp[0], dp[1] = 1, 1

        # starting from 3rd step, step 1 + step 2 = step 3
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # return last val in dp arr
        return dp[n]

n = 2

ob = Solution()
print(ob.climbStairs(n))