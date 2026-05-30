# co3_constraint_reasoning.py


# =====================================
# COMMON AI ENVIRONMENT
# =====================================

start_node = 'A'

goal_node = 'F'

blocked_nodes = ['C']

max_cost = 15

graph = {

    'A': [('B', 2), ('C', 4)],

    'B': [('E', 1), ('D', 5), ('C', 3)],

    'C': [('E', 6)],

    'D': [('E', 2)],

    'E': [('F', 3)],

    'F': []
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

    print("Maximum Allowed Cost :", max_cost)

    print("Expected Best Path : A -> B -> E -> F\n")


# =====================================
# VISITED SET
# =====================================

visited = set()


# =====================================
# CONSTRAINT CHECKING
# =====================================

def is_valid(node, total_cost):

    if node in blocked_nodes:

        print("\nConstraint Failed")

        print(node, "is blocked/risky")

        return False

    if total_cost > max_cost:

        print("\nConstraint Failed")

        print("Cost exceeded maximum limit")

        return False

    return True


# =====================================
# BACKTRACKING CSP SEARCH
# =====================================

def backtrack(node, total_cost, path):

    print("\nAI Visiting:", node)

    path.append(node)

    visited.add(node)

    print("Current Path:", path)

    print("Current Cost:", total_cost)

    if node == goal_node:

        print("\nGoal Reached:", node)

        return True

    for neighbor, cost in graph[node]:

        if neighbor not in visited:

            print("\nChecking Constraints for", neighbor)

            new_cost = total_cost + cost

            if is_valid(neighbor, new_cost):

                print("Constraint Accepted")

                result = backtrack(

                    neighbor,

                    new_cost,

                    path
                )

                if result:

                    return True

    path.pop()

    return False


# =====================================
# MAIN
# =====================================

display_graph()

path = []

backtrack(start_node, 0, path)

print("\n========== FINAL PATH ==========\n")

print(path)

