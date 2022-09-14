# 91. Decode Ways

def numDecodings(s: str) -> int:
  if s == '0': return 0
  if len(s) == 1: return 1
  dp = [0 for i in range(len(s)+1)]
  dp[0], dp[1] = 1,1
  for i in range(2,len(s)+1):
    if 0 < int(s[i-1:i]) < 10:
      dp[i] += dp[i-1]
    if 9 < int(s[i-2:i]) < 27:
      dp[i] += dp[i-2]

  return dp[-1]

s = "231"
print(numDecodings(s))
