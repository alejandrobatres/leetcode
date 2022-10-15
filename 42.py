# 42. Trapping Rain Water

def trap(height: list[int]) -> int:
  if len(height) < 3: return 0
  l, r = 0, len(height)-1
  lm, rm = height[l], height[r]
  res = 0
  while l < r:
    if lm < rm:
      l += 1
      lm = max(lm, height[l])
    else:
      r -= 1
      rm = max(rm, height[r])
    res += lm - height[l] if lm < rm else rm - height[r]
  return res


'''
Notes:
   
   Counting the water above a spot is counting the difference between minimum
   of both left and right maximums and the spot itself.

   When going through the list, we know that the current min on each size is
   going to be either the current max from the left and right.

'''
