# 416. Partition Equal Subset Sum

def canPartition(nums: list[int]) -> bool:
  if sum(nums) % 2: return False
  dp = {0}
  tsum = sum(nums)//2 # target since both sides must be equal (half of sum)
  for i in range(len(nums)):
    if tsum - nums[i] in dp: return True # check if other half of sum exists
    else:
      # add all new sums to dp
      temp = set()
      for e in dp:
        temp.add(e+nums[i])
      for e in temp:
        dp.add(e)
  return False


