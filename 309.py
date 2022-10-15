# 309. Best Time to Buy and Sell Stock with Cooldown

def maxProfit(prices: list[int]) -> int:
  dp = [[0]*len(prices) for i in range(len(prices))]

  for i in range(len(prices)):
    for j in range(len(prices)):

