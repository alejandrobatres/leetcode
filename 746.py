# 746. Min Cost Climbing Stairs

def minCostClimbingStairs(cost: list[int]) -> int:
  if len(cost) < 3: return min(cost)

  for i in range(2, len(cost)):
    cost[i] += min(cost[i-1],cost[i-2])
  return min(cost[-1], cost[-2])

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))
