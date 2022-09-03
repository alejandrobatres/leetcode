# 5. Longest Palindromic Substring

def longestPalindrome(s: str) -> str:
  # creating the dp of size s by s
  dp = [[False]*len(s) for i in range(len(s))]
  res = "" 
  # all slices length 1 are palidromes
  for i in range(len(s)):
    dp[i][i] = True
    res = s[i]

  # we are only going to traverse the top diagonal half of dp
  for i in range(len(s)-1, -1, -1):
    for j in range(i+1,len(s)):
      if s[i] == s[j]: # check if current characters are equal
        # check if characters are adjacent OR if inner str is valid
        dp[i][j] = ((j-i == 1) or dp[i+1][j-1])
        if len(res) < j - i: res = s[i:j+1] # change current largest

  return res

s = "babac"
print(longestPalindrome(s))
