# 213. House Robber II

def rob(nums: list[int]) -> int:
  if len(nums) < 3: return max(nums)
  prev, curr = 0, 0
  for i in range(len(nums)-1):
    prev, curr = curr, max(curr, prev + nums[i])

  res = curr
  prev, curr = 0, 0
  for i in range(1, len(nums)):
    prev, curr = curr, max(curr, prev + nums[i])

  return max(res, curr)

nums = [1,2,3]
print(rob(nums))
