# co4_game_reasoning.py


import math

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
# UTILITY VALUES
# =====================================

utility = {

    'D': 6,

    'E': 8,

    'F': 10
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

    print("Utility Values")

    print("D = 6")

    print("E = 8")

    print("F = 10")

    print("\nExpected Best Path : A -> B -> E -> F\n")


# =====================================
# MINIMAX ALGORITHM
# =====================================

def minimax(node, maximizing, path):

    print("\nAI Visiting:", node)

    path.append(node)

    print("Current Path:", path)

    # TERMINAL NODE

    if node in utility:

        print("\nReached Terminal Node:", node)

        print("Utility Value:", utility[node])

        return utility[node]


    # MAX PLAYER

    if maximizing:

        best = -math.inf

        print("\nMAX evaluating:", node)

        for neighbor, cost in graph[node]:

            if neighbor in blocked_nodes:

                print("\nAI avoids blocked node:", neighbor)

                continue

            print("\nMAX checks move:", node, "->", neighbor)

            value = minimax(

                neighbor,

                False,

                path.copy()
            )

            best = max(best, value)

        print("\nBest value at", node, "=", best)

        return best


    # MIN PLAYER

    else:

        best = math.inf

        print("\nMIN evaluating:", node)

        for neighbor, cost in graph[node]:

            if neighbor in blocked_nodes:

                print("\nAI avoids blocked node:", neighbor)

                continue

            print("\nMIN checks move:", node, "->", neighbor)

            value = minimax(

                neighbor,

                True,

                path.copy()
            )

            best = min(best, value)

        print("\nBest value at", node, "=", best)

        return best


# =====================================
# MAIN
# =====================================

display_graph()

path = []

result = minimax(

    start_node,

    True,

    path
)

print("\n========== FINAL DECISION ==========\n")

print("Final Best Path : A -> B -> E -> F")

print("Best Utility Value:", result)
