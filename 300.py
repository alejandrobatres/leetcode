# 300. Longest Increasing Subsequence

def lengthOfLIS(nums: list[int]) -> int:
  if len(nums) == 1: return 1
  dp = [1]*len(nums)

  for i in range(1,len(nums)):
    for j in range(i):
      if nums[j] < nums[i]:
        dp[i] = max(dp[j]+1, dp[i])
  return max(dp)
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
