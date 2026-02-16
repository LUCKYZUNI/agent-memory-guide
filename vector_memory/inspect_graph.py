import json
import networkx as nx
import os
import sys

GRAPH_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory_graph.json")

def inspect():
    if not os.path.exists(GRAPH_FILE):
        print("❌ Graph file not found.")
        return

    with open(GRAPH_FILE, 'r') as f:
        data = json.load(f)
    
    g = nx.node_link_graph(data)
    
    print(f"🕸️  Graph Stats: {g.number_of_nodes()} Nodes, {g.number_of_edges()} Edges")
    
    print("\n📍 Nodes:")
    for n in g.nodes(data=True):
        print(f"  - {n[0]} ({n[1].get('type', 'unknown')})")

    print("\n🔗 Edges:")
    for u, v, data in g.edges(data=True):
        print(f"  - {u} --[{data.get('relation', 'related')}]--> {v}")

    print("\n🔍 Example Queries:")
    # Helper to print neighbors
    def show_related(node):
        if node not in g:
            print(f"  '{node}' not found in graph.")
            return
        print(f"  Neighbors of '{node}':")
        for n in g.successors(node):
            print(f"    -> {n} ({g.get_edge_data(node, n).get('relation')})")
        for n in g.predecessors(node):
            print(f"    <- {n} ({g.get_edge_data(n, node).get('relation')})")

    print("• 'Universal Human-Like Bot vision' (Approximated as 'Projects' or 'Strategy & Directives')")
    show_related("Projects") # Likely node
    
    print("• 'Architecture decisions'")
    show_related("Research & Architecture")

if __name__ == "__main__":
    inspect()
