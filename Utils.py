import json


def save_path_to_file(path, filename="path.txt"):
    """
    Save optimized path to a text file.

    Args:
        path: list of (x, y) tuples representing the path
        filename: name of file to save to (default: "path.txt")
    """
    with open(filename, 'w') as f:
        json.dump(path, f)


def load_path_from_file(filename="path.txt"):
    """
    Load path from a text file.

    Args:
        filename: name of file to load from (default: "path.txt")

    Returns:
        list of (x, y) tuples, or None if file doesn't exist
    """
    import os

    if not os.path.exists(filename):
        print("No existing path found. Need to discover maze first.")
        return None

    with open(filename, 'r') as f:
        path_data = json.load(f)

    # Convert back to tuples
    path = [tuple(point) for point in path_data]

    print("Loaded existing path from path.txt")
    print(f"  Path length: {len(path)} waypoints")
    print(f"  Path: {path}")

    return path

def optimize_path(path):
    """
    Optimize path by removing intermediate points in straight lines.
    Keeps only points where direction changes.

    Args:
        path: list of (x, y) tuples representing the path

    Returns:
        optimized_path: list of (x, y) tuples with intermediate points removed

    Example:
        Input:  [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2)]
        Output: [(0,0), (3,0), (3,2)]
    """
    if len(path) <= 2:
        return path

    optimized = [path[0]]  # Always keep start point

    for i in range(1, len(path) - 1):
        prev_point = path[i - 1]
        current_point = path[i]
        next_point = path[i + 1]

        # Calculate direction vectors
        dx1 = current_point[0] - prev_point[0]
        dy1 = current_point[1] - prev_point[1]

        dx2 = next_point[0] - current_point[0]
        dy2 = next_point[1] - current_point[1]

        # Keep point if direction changes
        if dx1 != dx2 or dy1 != dy2:
            optimized.append(current_point)

    optimized.append(path[-1])  # Always keep end point

    return optimized
