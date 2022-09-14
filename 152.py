# 152. Maximum Product Subarray

def maxProduct(nums: list[int]) -> int:
  res = nums[0]
  curr_min, curr_max = nums[0], nums[0]

  for i in range(1,len(nums)):
    temp_max = curr_max
    curr_max = max(nums[i], curr_max*nums[i], curr_min*nums[i])
    curr_min = min(nums[i], temp_max*nums[i], curr_min*nums[i])
    res = max(res, curr_max)
  return res

nums = [2,3,-2,4]
print(maxProduct(nums))
