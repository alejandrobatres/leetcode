# 131. Palindromic Partitioning

def partition(s: str) -> list[list[str]]:
  res = []
  sub = []
  p = ""

  def helper(i,p):
    if i >= len(s):
      res.append(sub.copy())
      return
    p += s[i]
    if p == p[::-1]:
      sub.append(p)
    helper(i+1,p)
    p = s[:-1]
    helper(i+1,p)
  
  helper(0,p)
  return res

s = "aab"
print(partition(s))

