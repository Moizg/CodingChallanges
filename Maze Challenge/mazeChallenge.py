def canExit(maze):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or maze[r][c] == 1 or (r, c) in visited:
            return False
        if (r, c) == (rows - 1, cols - 1):
            return True

        visited.add((r, c))
        return (
            dfs(r+1, c) or
            dfs(r-1, c) or
            dfs(r, c+1) or
            dfs(r, c-1)
        )

    return dfs(0, 0)


print(canExit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]))
#output = True

print(canExit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]))
#output = False
# This maze only has dead ends!

print(canExit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]))
#output = False

# Exit only one block away, but unreachable!

print(canExit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]))
#output = True