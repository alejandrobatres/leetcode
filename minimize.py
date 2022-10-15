
def minimize(point, k):
  avg = sum(point)/len(point)
  for i in range(len(point)):
    diff = min(abs(point[i]+k-avg),abs(point[i]-k-avg))
    if diff == abs(point[i]+k-avg):
      point[i] += k
    else:
      point[i] -= k
  return max(point)-min(point)

point = [0,1,2,3]
k = 2
print(minimize(point, k))
