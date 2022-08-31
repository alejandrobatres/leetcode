# 40. Combination Sum II

def combinationSum2(candidates: list, target: int) -> list[list[int]]:
  if sum(candidates) < target: return []
  res = []
  sub = []
  curr_sum = [0]
  candidates.sort()

  def helper(i):
    if curr_sum[0] == target:
      res.append(sub.copy())
      return
    if i >= len(candidates) or curr_sum[0] > target:
      return
    sub.append(candidates[i])
    curr_sum[0] += candidates[i]
    helper(i+1)

    sub.pop()
    curr_sum[0] -= candidates[i]
    temp = candidates[i]
    while i < len(candidates) and temp == candidates[i]:
      i += 1
    helper(i)
  helper(0)
  return res

candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27
print(combinationSum2(candidates, target))

