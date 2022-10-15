# 62. Unique Paths

def uniquePaths(m: int, n: int) -> int:
  dp = [[0]*(m+1) for i in range(n+1)]
  dp[1][1] = 1
  for i in range(1, m+1):
    for j in range(1, n+1):
      dp[i][j] += dp[i-1][j] + dp[i][j-1] + 1
  return dp[m][n]
