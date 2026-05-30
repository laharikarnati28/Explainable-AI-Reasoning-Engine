# co1_agent_reasoning.py


from dataclasses import dataclass
from typing import Dict, List

# =====================================
# COMMON AI ENVIRONMENT
# =====================================

start_node = 'A'

goal_node = 'F'

blocked_nodes = ['C']

graph: Dict[str, List[str]] = {

    'A': ['B', 'C'],

    'B': ['E', 'D', 'C'],

    'C': ['E'],

    'D': ['E'],

    'E': ['F'],

    'F': []
}


# =====================================
# PEAS MODEL
# =====================================

class PEAS:

    def __init__(self):

        self.performance = "Reach goal node correctly"

        self.environment = "Weighted Graph Environment"

        self.actuators = [
            "Move to node",
            "Explain reasoning"
        ]

        self.sensors = [
            "Current node",
            "Graph information"
        ]

    def display(self):

        print("\n========== PEAS MODEL ==========\n")

        print("Performance :", self.performance)

        print("Environment :", self.environment)

        print("Actuators   :", self.actuators)

        print("Sensors     :", self.sensors)

        print("\n================================\n")


# =====================================
# STATE REPRESENTATION
# =====================================

@dataclass
class State:

    current_node: str


# =====================================
# DISPLAY GRAPH
# =====================================

def display_graph():

    print("\n=============== GRAPH ===============\n")

    print("                A")

    print("             /     \\")

    print("          2 /       \\ 4")

    print("           /         \\")

    print("          B -----3---- C")

    print("         / \\           \\")

    print("      5 /   \\1          \\6")

    print("       /     \\           \\")

    print("      D -----2----------- E")

    print("               \\")

    print("                \\3")

    print("                 \\")

    print("                  F")

    print("\n=====================================\n")

    print("Initial Node :", start_node)

    print("Goal Node :", goal_node)

    print("Blocked/Risky Node :", blocked_nodes)

    print("Expected Best Path : A -> B -> E -> F\n")


# =====================================
# DFS REASONING
# =====================================

def dfs(node, visited, path):

    print("\nAI Visiting:", node)

    visited.add(node)

    path.append(node)

    print("Current Path:", path)

    if node == goal_node:

        print("\nGoal Reached:", node)

        return True

    for neighbor in graph[node]:

        if neighbor not in visited:

            if neighbor in blocked_nodes:

                print("\nAI avoids blocked node:", neighbor)

                continue

            print("\nReasoning Step")

            print(node, "can move to", neighbor)

            print("AI selects", neighbor)

            result = dfs(neighbor, visited, path)

            if result:

                return True

    path.pop()

    return False


# =====================================
# MAIN
# =====================================

peas = PEAS()

peas.display()

display_graph()

visited = set()

path = []

dfs(start_node, visited, path)

print("\n========== FINAL PATH ==========\n")

print(path)

