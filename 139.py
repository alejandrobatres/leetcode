# 139. Word Break

def wordBreak(s: str, wordDict: list[str]) -> bool:
  wordl = set(wordDict)
  dp = [False] * (len(s)+1)
  dp[0] = True

  for i in range(len(s)):
    for j in range(i, len(s)):
      dp[j+1] = True if dp[i] and s[i:j+1] in wordl else dp[j+1]

  return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))
