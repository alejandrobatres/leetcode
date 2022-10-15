# 1143. Longest Common Subsequence

def longestCommonSubsequence(text1: str, text2: str) -> int:

  dp = [[0]*(len(text1)+1) for i in range(len(text2)+1)] # extra dim for 0s
  
  for i in range(1,len(text2)+1):
    for j in range(1,len(text1)+1):
      if i != 0 or j != 0: # ignore first row and col
        if text1[j] == text2[j]: # if char equal we add to previous count for both
          dp[i][j] = dp[i-1][j-1] + 1
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # carry highest from each
  return dp[-1][-1]
