# co6_hybrid_reasoning_engine.py


import heapq

# =====================================
# COMMON AI ENVIRONMENT
# =====================================

start_node = 'A'

goal_node = 'F'

blocked_nodes = ['C']

graph = {

    'A': [('B', 2), ('C', 4)],

    'B': [('E', 1), ('D', 5), ('C', 3)],

    'C': [('E', 6)],

    'D': [('E', 2)],

    'E': [('F', 3)],

    'F': []
}


# =====================================
# HEURISTIC VALUES
# =====================================

heuristic = {

    'A': 7,

    'B': 5,

    'C': 100,

    'D': 3,

    'E': 1,

    'F': 0
}


# =====================================
# SAFETY PROBABILITIES
# =====================================

safe_probability = {

    'B': 0.90,

    'C': 0.20,

    'D': 0.80,

    'E': 0.85,

    'F': 0.95
}


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
# CONSTRAINT CHECKING
# =====================================

def is_valid(node):

    if node in blocked_nodes:

        print("\nConstraint Failed")

        print(node, "is blocked/risky")

        return False

    return True


# =====================================
# HYBRID AI REASONING
# =====================================

def hybrid_astar(start, goal):

    pq = []

    heapq.heappush(

        pq,

        (0, start, [start], 0)
    )

    visited = set()

    while pq:

        f, node, path, current_cost = heapq.heappop(pq)

        print("\n================================")

        print("AI Expanding:", node)

        print("Current Path:", path)

        print("Current Cost:", current_cost)

        print("================================")

        if node == goal:

            print("\nGoal Reached Successfully")

            print("Final Path:", path)

            return path

        if node not in visited:

            visited.add(node)

            for neighbor, cost in graph[node]:

                print("\nChecking Neighbor:", neighbor)

                # CONSTRAINT CHECK

                if not is_valid(neighbor):

                    continue

                # PROBABILITY CHECK

                probability = safe_probability[neighbor]

                print("Safety Probability =", probability)

                if probability < 0.5:

                    print("AI avoids risky node")

                    continue

                # HEURISTIC SEARCH

                g = current_cost + cost

                h = heuristic[neighbor]

                total = g + h

                print("\nReasoning Step")

                print("Move:", node, "->", neighbor)

                print("Actual Cost g(n) =", g)

                print("Heuristic h(n) =", h)

                print("Final Cost f(n) =", total)

                print("AI selects safest optimal path")

                heapq.heappush(

                    pq,

                    (

                        total,

                        neighbor,

                        path + [neighbor],

                        g
                    )
                )

    print("\nNo Path Found")


# =====================================
# MAIN
# =====================================

display_graph()

final_path = hybrid_astar(

    start_node,

    goal_node
)

print("\n========== FINAL AI DECISION ==========\n")

print("Final Best Path : A -> B -> E -> F")

