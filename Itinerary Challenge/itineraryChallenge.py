from collections import defaultdict

def findPath(tickets):
    # Build adjacency list
    graph = defaultdict(list)
    for f, t in tickets:
        graph[f].append(t)

    # Sort destinations alphabetically for each departure
    for f in graph:
        graph[f].sort()

    total_tickets = len(tickets)
    route = ["A"]
    result = None  # store final route once found

    def dfs(current):
        nonlocal result

        # If all tickets used, save result
        if len(route) == total_tickets + 1:
            result = route[:]
            return True

        # Explore all possible destinations from current
        for i in range(len(graph[current])):
            next_dest = graph[current][i]
            if next_dest is None:
                continue  # skip used ticket

            # Mark ticket as used
            graph[current][i] = None
            route.append(next_dest)

            if dfs(next_dest):
                return True  # stop at first valid lexicographically smallest route

            # Backtrack
            route.pop()
            graph[current][i] = next_dest

        return False

    dfs("A")
    return result


# 🔍 Tests
print(findPath([["C", "F"], ["A", "C"], ["I", "Z"], ["F", "I"]]))
# ➤ ["A", "C", "F", "I", "Z"]

print(findPath([["A","C"],["A","B"],["C","B"],["B","A"],["B","C"]]))
# ➤ ["A","B","A","C","B","C"]

print(findPath([["Y", "L"], ["D", "A"], ["A", "D"], ["R", "Y"], ["A", "R"]]))
# ➤ ["A", "D", "A", "R", "Y", "L"]