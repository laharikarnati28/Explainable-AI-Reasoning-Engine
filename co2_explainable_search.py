# co2_explainable_search.py


from queue import Queue
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
# BFS SEARCH
# =====================================

def bfs(start):

    print("\n========== BFS SEARCH ==========\n")

    q = Queue()

    q.put((start, [start]))

    visited = set()

    while not q.empty():

        node, path = q.get()

        if node not in visited:

            if node in blocked_nodes:

                print("AI avoids blocked node:", node)

                continue

            print("\nAI Exploring:", node)

            print("Current Path:", path)

            visited.add(node)

            if node == goal_node:

                print("\nGoal Reached:", node)

                print("Final Path:", path)

                return

            for neighbor, cost in graph[node]:

                print(

                    "Reason:",

                    node,

                    "can move to",

                    neighbor
                )

                q.put(

                    (

                        neighbor,

                        path + [neighbor]
                    )
                )


# =====================================
# UCS SEARCH
# =====================================

def ucs(start):

    print("\n========== UCS SEARCH ==========\n")

    pq = []

    heapq.heappush(

        pq,

        (0, start, [start])
    )

    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node not in visited:

            if node in blocked_nodes:

                print("AI avoids blocked node:", node)

                continue

            visited.add(node)

            print("\nSelected Node:", node)

            print("Current Cost:", cost)

            print("Current Path:", path)

            if node == goal_node:

                print("\nGoal Reached:", node)

                print("Final Path:", path)

                return

            for neighbor, edge_cost in graph[node]:

                total = cost + edge_cost

                print(

                    "AI compares total cost:",

                    total
                )

                heapq.heappush(

                    pq,

                    (

                        total,

                        neighbor,

                        path + [neighbor]
                    )
                )


# =====================================
# A* SEARCH
# =====================================

def astar(start, goal):

    print("\n========== A* SEARCH ==========\n")

    pq = []

    heapq.heappush(

        pq,

        (0, start, [start], 0)
    )

    visited = set()

    while pq:

        f, node, path, current_cost = heapq.heappop(pq)

        if node in blocked_nodes:

            print("\nAI avoids blocked node:", node)

            continue

        print("\nExpanding Node:", node)

        print("Current Path:", path)

        if node == goal:

            print("\nGoal Reached:", node)

            print("Final Path:", path)

            return

        if node not in visited:

            visited.add(node)

            for neighbor, cost in graph[node]:

                g = current_cost + cost

                h = heuristic[neighbor]

                total = g + h

                print("\nReasoning Step")

                print("Move:", node, "->", neighbor)

                print("Actual Cost g(n) =", g)

                print("Heuristic h(n) =", h)

                print("Final Cost f(n) =", total)

                heapq.heappush(

                    pq,

                    (

                        total,

                        neighbor,

                        path + [neighbor],

                        g
                    )
                )


# =====================================
# MAIN
# =====================================

display_graph()

bfs(start_node)

ucs(start_node)

astar(start_node, goal_node)

