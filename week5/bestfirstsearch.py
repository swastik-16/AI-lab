import heapq
def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
def best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    priority_queue = []
    heapq.heappush(priority_queue, (manhattan_distance(start[0], start[1], goal[0], goal[1]), start))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while priority_queue:
        current = heapq.heappop(priority_queue)