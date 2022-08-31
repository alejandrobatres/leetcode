# 198. House Robber

def rob(nums: list[int]) -> int:
  prev, curr = 0, 0
  for i in nums:
    prev, curr = curr, max(n+prev, curr)
  return curr

nums = [2,7,9,3,1]
print(rob(nums))
