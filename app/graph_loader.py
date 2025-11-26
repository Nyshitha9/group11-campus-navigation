import json
from pathlib import Path

# This path will be used later when real data is added
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "campus_map.json"

def load_campus_map(path=None):
    """
    Sprint-1 Skeleton:
    ------------------
    This function will later load the real campus map from a JSON file.

    For now, I'm demonstrating the intended behaviour:
    - Choose the JSON file path
    - Try to open it
    - Return an empty structure if file not ready yet

    """

    p = Path(path) if path else DATA_PATH

    # If file does not exist, return an empty campus map structure
    if not p.exists():
        return {"nodes": [], "edges": []}

    # Minimal demonstration logic (not full implementation)
    with open(p, "r", encoding="utf-8") as fh:
        return json.load(fh)


def build_graph(data):
    """

    This function will  convert JSON campus map data into
    a graph (adjacency list). 

    Full logic  I'll implement by Sprint-2.
    """

    # Extract node IDs (placeholder)
    nodes = {n.get("id", f"node_{i}"): n for i, n in enumerate(data.get("nodes", []))}

    # Create empty adjacency list (no edges yet)
    adjacency = {nid: {} for nid in nodes.keys()}


    # (Actual edge linking will be done in Sprint-2)
    return adjacency, nodes
