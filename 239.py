# 239. Sliding Window Maximum

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
  if k == 1: return nums

  counts = Counter(nums[:k])
  heap = []
  for e in counts.keys():
    heapq.heappush(heap, -1*e)

  res = [-1*heap[0]] # initialize with first max

  for i in range(k, len(nums)):
    e, p = nums[i], nums[i-k] # next element and previous
    heapq.heappush(heap, -1*e) # add new element to heap and map
    counts[e] = counts.get(e, 0) + 1 
    counts[p] -= 1 # decrement / remove old element from map
    if counts[p] == 0: del counts[p]

    while -1*heap[0] not in counts: # remove old maxes
      heapq.heappop(heap)

    res.append(-1*heap[0]) # add current max

  return res

