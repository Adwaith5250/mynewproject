from heapq import heappop, heappush


def greedy_best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = []
    heappush(priority_queue, (heuristics[start], start, [start]))

    while priority_queue:
        _, node, path = heappop(priority_queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heappush(priority_queue, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

heuristics = {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 7,
    "E": 1,
    "F": 0
}

path = greedy_best_first_search(graph, heuristics, "A", "F")

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")
