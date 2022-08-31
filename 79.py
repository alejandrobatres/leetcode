# 79. Word Search


def exist(board: list[list[str]], word: str) -> bool:
  exists = [False] 
  seen = set()
  def dfs(i, j, k):
    if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]) or k >= len(word): return
    if board[i][j] != word[k]: return
    if k == len(word) - 1:
      exists[0] = True
      return
    seen.add((i, j))
    if (i+1, j) not in seen: dfs(i+1, j, k+1)
    if (i-1, j) not in seen: dfs(i-1, j, k+1)
    if (i, j+1) not in seen: dfs(i, j+1, k+1)
    if (i, j-1) not in seen: dfs(i, j-1, k+1)
    seen.remove((i, j))

  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == word[0]:
        dfs(i, j, 0)
        if exists[0]: return True
  return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))
