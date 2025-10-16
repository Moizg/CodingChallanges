def trace_word_path(word, grid):
    rows = len(grid)
    cols = len(grid[0])

    # Only 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def backtrack(r, c, index, path, visited):
        # Base case — found full word
        if index == len(word):
            return path

        # Boundary and validity checks
        if not (0 <= r < rows and 0 <= c < cols):
            return None
        if grid[r][c] != word[index] or (r, c) in visited:
            return None

        # Mark visited and store coordinate
        visited.add((r, c))
        path.append([r, c])

        # Explore 4 directions
        for dr, dc in directions:
            result = backtrack(r + dr, c + dc, index + 1, path, visited)
            if result:
                return result

        # Backtrack (undo)
        path.pop()
        visited.remove((r, c))
        return None

    # Try each cell as starting position
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                path = []
                visited = set()
                result = backtrack(r, c, 0, path, visited)
                if result:
                    return result

    return "Not present"


print(trace_word_path("BISCUIT", [
  ["B", "I", "T", "R"],
  ["I", "U", "A", "S"],
  ["S", "C", "V", "W"],
  ["D", "O", "N", "E"]
]))
# → [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [0, 1], [0, 2]]

print(trace_word_path("HELPFUL", [
  ["L","I","T","R"],
  ["U","U","A","S"],
  ["L","U","P","O"],
  ["E","F","E","H"]
]))
# → "Not present"

print(trace_word_path("UKULELE", [
  ["N", "H", "B", "W"],
  ["E", "X", "A", "D"],
  ["L", "A", "U", "U"],
  ["E", "L", "U", "K"]
]))
# → [[2, 3], [3, 3], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0]]

print(trace_word_path("SURVIVAL", [
  ["V", "L", "R", "L"],
  ["V", "A", "I", "V"],
  ["I", "O", "S", "C"],
  ["V", "R", "U", "F"]
]))
# → [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [0, 1]]