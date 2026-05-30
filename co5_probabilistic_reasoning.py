# co5_probabilistic_reasoning.py


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
# BAYES PROBABILITY FUNCTION
# =====================================

def bayes(p_a, p_b_given_a, p_b):

    result = (

        p_b_given_a * p_a

    ) / p_b

    return result


# =====================================
# AI PROBABILITY REASONING
# =====================================

def probability_reasoning(path):

    print("\n========== AI PROBABILITY REASONING ==========\n")

    total_probability = 1

    for node in path:

        if node in safe_probability:

            probability = safe_probability[node]

            print("\nChecking Node:", node)

            print("Safety Probability =", probability)

            if node in blocked_nodes:

                print("AI marks node as risky")

                continue

            print("AI believes node is SAFE")

            total_probability *= probability

    print("\nOverall Path Safety Probability =")

    print(round(total_probability, 4))


# =====================================
# MARKOV STYLE TRANSITIONS
# =====================================

def markov_demo(path):

    print("\n========== STATE TRANSITIONS ==========\n")

    for i in range(len(path) - 1):

        print(

            path[i],

            "->",

            path[i + 1]
        )

    print("\nAI selects safest path")


# =====================================
# MAIN
# =====================================

display_graph()

final_path = [

    'A',

    'B',

    'E',

    'F'
]

probability_reasoning(final_path)

markov_demo(final_path)

print("\n========== FINAL AI DECISION ==========\n")

print("Final Safe Path : A -> B -> E -> F")

