class Solution(object):
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')
        
        # dp[i][j][k] = max coins at (i,j) with k neutralizations left
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base case: starting cell
        dp[0][0][2] = coins[0][0]           # took value normally
        if coins[0][0] < 0:
            dp[0][0][1] = 0                 # neutralized it (used 1 skip)
        
        # Fill first row (can only come from left)
        for j in range(1, n):
            for k in range(3):
                prev = dp[0][j-1][k]
                if prev == NEG_INF:
                    continue
                # Option 1: take the cell value
                dp[0][j][k] = max(dp[0][j][k], prev + coins[0][j])
                # Option 2: neutralize (only if robber cell and k > 0)
                if coins[0][j] < 0 and k > 0:
                    dp[0][j][k-1] = max(dp[0][j][k-1], prev)
        
        # Fill first column (can only come from above)
        for i in range(1, m):
            for k in range(3):
                prev = dp[i-1][0][k]
                if prev == NEG_INF:
                    continue
                dp[i][0][k] = max(dp[i][0][k], prev + coins[i][0])
                if coins[i][0] < 0 and k > 0:
                    dp[i][0][k-1] = max(dp[i][0][k-1], prev)
        
        # Fill rest of grid
        for i in range(1, m):
            for j in range(1, n):
                for k in range(3):
                    best_prev = max(dp[i-1][j][k], dp[i][j-1][k])
                    if best_prev == NEG_INF:
                        continue
                    # Option 1: take value
                    dp[i][j][k] = max(dp[i][j][k], best_prev + coins[i][j])
                    # Option 2: neutralize
                    if coins[i][j] < 0 and k > 0:
                        dp[i][j][k-1] = max(dp[i][j][k-1], best_prev)
        
        return max(dp[m-1][n-1])