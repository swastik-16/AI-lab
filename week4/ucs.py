import heapq

def uniform_cost_search(graph, start, goal):
    """Find the minimum-cost path between start and goal nodes using UCS."""
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        
        path = path + [current_node]

        if current_node == goal:
            return cost, path


        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return float("inf"), []  

graph = {
    "Delhi": [("Jaipur", 71), ("Kota", 151)],
    "Jaipur": [("Delhi", 71), ("Jodhpur", 75)],
    "Jodhpur": [("Jaipur", 75), ("Ahmedabad", 118), ("Kota", 140)],
    "Kota": [("Delhi", 151), ("Jodhpur", 140), ("Bhopal", 80), ("Jhansi", 99)],
    "Ahmedabad": [("Jodhpur", 118), ("Nasik", 111)],
    "Nasik": [("Ahmedabad", 111), ("Mumbai", 70)],
    "Mumbai": [("Nasik", 70), ("Pune", 75)],
    "Pune": [("Mumbai", 75), ("Solapur", 120)],
    "Solapur": [("Pune", 120), ("Amravati", 138), ("Bhopal", 146)],
    "Bhopal": [("Kota", 80), ("Amravati", 97), ("Solapur",146)],
    "Jhansi": [("Kota", 99), ("Hyderabad", 211)],
    "Amravati": [("Bhopal", 97), ("Solapur", 138), ("Hyderabad", 101)],
    "Hyderabad": [("Amravati", 101), ("Jhansi", 211), ("Warangal", 85), ("Kurnool", 90)],
    "Warangal": [("Hyderabad", 85), ("Visakapatnam", 98), ("Bhilai",142)],
    "Kurnool": [("Hyderabad", 90)],
    "Visakapatnam": [("Warangal", 98), ("Vijaywada", 86)],
    "Vijayawada": [("Vishakapatnam", 86)],
    "Bhilai": [("Warangal", 142), ("Raipur", 92)],
    "Raipur": [("Bhilai", 92), ("Bilaspur", 87)],
    "Bilaspur": [("Raipur", 87)],
}

start = "Delhi"
goal = "Pune"
cost, path = uniform_cost_search(graph, start, goal)
print(f"Minimum cost: {cost}")
print(f"Path: {' -> '.join(path)}")
