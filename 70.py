# 70. Climbing Stairs

def climbStairs(n: int) -> int:
  prev = 0
  curr = 1
  for i in range(n):
    prev, curr = curr, prev + curr
  return curr

  n = 5
  print(climbStairs(n))
