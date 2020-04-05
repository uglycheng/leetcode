class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        # dp[i] represents the max value the current player can get from stoneValue[i:]
        # because the game start with Alice, so if dp[0] can get above half the total values , Alice win
        # if you want to get the exact strategy for Alice to win, because we have the array dp,
        # no matter how Bob take action, Alice just need to reaction according to the opnent_min_value = min(dp[i+1],dp[i+2],dp[i+3])
        dp = [0 for i in range(len(stoneValue))]+[0,1001,1001,1001]
        sum_ = 0
        for i in range(len(stoneValue)-1,-1,-1):
            sum_ += stoneValue[i]
            opnent_min_value = min(dp[i+1],dp[i+2],dp[i+3])
            dp[i] = sum_ - opnent_min_value
        if dp[0] + dp[0] > sum_:
            return "Alice"
        elif dp[0] + dp[0] < sum_:
            return "Bob"
        else:
            return "Tie"