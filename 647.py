# 647. Palindromic Substrings

def countSubstrings(s: str) -> int:
  res = 0
  dp = [[False]*len(s) for i in range(len(s))]

  for i in range(len(s)):
    res += 1 # each char is a palindrome
    dp[i][i] = True

  for i in range(len(s)-1,-1,-1)):
    for j in range(i+1, len(s)): # don't need to go through diag
      if s[i]==s[j]:
        if j-i==1 or dp[i+1][j-1]:
          dp[i][j] = True
          res += 1

  return res

s = "aaa"
print(countSubstrings(s))
