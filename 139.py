# 139. Word Break

def wordBreak(s: str, wordDict: list[str]) -> bool:
  i, j = 0, 0
  d = set(wordDict)

  while i < len(s):
    if s[j:i+1] in d:
      j = i+1
    i += 1
  
  return j == i
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))
