import math
import heapq
from collections import deque


def straight_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


class Path:
    def __init__(self, node_id=None, previous=None, cost=0, estimation=0):
        self.previous = previous
        self.node_id = node_id
        self.cost = cost
        self.estimation = estimation

    def expand(self, node_id, added_cost, estimation):
        return Path(node_id, self, self.cost + added_cost, estimation)

    def get_heuristic_distance(self):
        return self.cost + self.estimation

    def __eq__(self, other):
        if isinstance(other, Path):
            return self.get_heuristic_distance() == other.get_heuristic_distance()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Path):
            return self.get_heuristic_distance() < other.get_heuristic_distance()
        return NotImplemented


def get_path(end_of_path, goal):
    if end_of_path is None or end_of_path.node_id != goal:
        return []

    path = deque([])
    node = end_of_path
    while node:
        path.appendleft(node.node_id)
        node = node.previous

    return list(path)


def shortest_path(M,start,goal):
    print(f"Shortest path from {start} to {goal} called")

    if M is None or M.intersections is None or start not in M.intersections or goal not in M.intersections:
        print(f"Intersections {start} or {goal} not found in map")
        return []

    result    = None
    frontier  = [Path(start)]
    explored  = set()
    goal_node = M.intersections[goal]

    while frontier:
        path    = heapq.heappop(frontier)
        node_id = path.node_id
        node    = M.intersections[node_id]

        if node_id == goal:
            result = path
            break

        explored.add(node_id)

        for neighbor_id in M.roads[node_id]:

            if neighbor_id not in explored:

                neighbor_node      = M.intersections[neighbor_id]
                cost_to_neighbor   = straight_distance(node, neighbor_node)
                estimation_to_goal = straight_distance(neighbor_node, goal_node)

                expanded_path = path.expand(neighbor_id, cost_to_neighbor, estimation_to_goal)

                heapq.heappush(frontier, expanded_path)

    return get_path(result, goal)


test_cases = [
    (map_10, 20, 30, []),
    (map_10, 8, 30, []),
    (map_10, 20, 8, []),

    (map_10, 8, 6, []),
    (map_10, 8, 9, [8, 9]),
    (map_10, 4, 6, [4, 3, 5, 0, 6]),

    (map_40, 5, 34, [5, 16, 37, 12, 34]),
    (map_40, 5, 5, [5]),
    (map_40, 8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]


for input_map, start, goal, solution in test_cases:
    result = shortest_path(input_map, start, goal)
    print("Calculated path")
    show_map(input_map, start, goal, result)
    print("Solution")
    show_map(input_map, start, goal, solution)
    print("result   =", result)
    print("Pass\n") if result == solution else print(f"expected = {solution}\n")


input_map = map_40
for start in range(len(input_map.intersections)):
    for goal in range(start, len(input_map.intersections)):
        print()
        result = shortest_path(input_map, start, goal)
        print(result)
        result_reversed = shortest_path(input_map, goal, start)
        print(result_reversed)
        assert result[::-1] == result_reversed