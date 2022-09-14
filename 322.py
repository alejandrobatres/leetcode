# 322. Coin Change

def coinChange(coins: list[int], amount: int) -> int:
  if amount == 0: return 0
  if len(coins) == 1: return -1 if amount%coins[0] != 0 else amount//coins[0]
  dp = [amount+1]*amount
   
  for c in coins:
    if amount >= c: dp[c-1] = 1
  
  for i in range(amount):
    for c in coins:
      if i >= c:
        dp[i] = min(dp[i-c]+1,dp[i])
  
  return dp[-1] if dp[-1] != amount+1 else -1
coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))
