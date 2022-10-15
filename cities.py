
def cities(red, blue, blueCost):
  dp = [[0]*len(blue) for i in range(len(red))]
  dp[0][0] = min(red[0], blue[0]+blueCost) 

  for i in range(1,len(red)):
    dp[i][0] = dp[i-1][0] + red[i]

  for i in range(1, len(blue)):
    dp[0][i] = dp[0][i-1] + blue[i]
 
  for i in range(len(red)):
    for j in range(len(blue)):
      dp[i][j] = min(dp[i-1][j], dp[i][j-1]+blueCost)
  return dp[-1][-1]

red = [2,3,4]
blue = [3,1,1]
blueCost = 2

print(cities(red, blue, blueCost))
