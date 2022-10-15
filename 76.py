# 76. Minimum Window Substring
from collections import Counter

def minWindow(s: str, t:str) -> str:
  if t == "": return ""
  if len(s) == 1: return s if t == s else ""
 
  t = Counts(t)
  temp = {k:0 for k in t}

  l, r = 0, 0
  
  res = [l, r]
  ml = 1000000
  
  c, n = 0, len(t) # count and needed count
  while r < len(s):
    e = s[r]
    if e in t:
      temp[e] += 1
      if temp[e] == t[e]: c += 1
    
    while c == n: # once condition met, remove any extras at front
      if r-l+1 < ml:
        ml = r-l+1
        res = [l, r]
      e = s[l]
      if e in t:
        temp[e] -= 1
        if t[e] < temp[e]:
          c -= 1
      l += 1
    r += 1

  return s[res[0]:res[1]+1] if ml != 1000000 else ""
