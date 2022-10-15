# 11. Container With Most Water

def maxArea(height: list[int]) -> int:
  l, r = 0, len(height)-1 # set pointers to opposite ends
  ma = 0 # initial max to 0

  while l < r:
    ca = min(height[l], height[r])*(r-l) # current area between both pointers
    ma = max(ma, ca)
    if height[l] < height[r]: l += 1 # keeping the larger height
    else: r -= 1

  return ma

'''
Notes: 

  The key here is that when we decrease the w of the rectangle
  the width no longer can contribute to a larger area so we 
  only have to worry about the heights.

'''
