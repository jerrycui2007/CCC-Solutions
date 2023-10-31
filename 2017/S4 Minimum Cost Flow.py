# https://dmoj.ca/problem/ccc17s4
# Doesn't get last subtask
from math import inf

buildings, pipes, enhancer_strength = list(map(int, input().split()))

adjacency_matrix = [[None for _ in range(buildings)] for _ in range(buildings)]

original_pipes = []
pipes_needed = []
pipe_activations = 0
pipe_deactivations = 0

# -1 for zero-indexing
for _ in range(buildings - 1):  # activated pipes
    start, end, cost = list(map(int, input().split()))
    adjacency_matrix[start - 1][end - 1] = (cost, True)
    adjacency_matrix[end - 1][start - 1] = (cost, True)
    original_pipes.append((start - 1, end - 1))

for _ in range(pipes - buildings + 1):  # inactive pipes
    start, end, cost = list(map(int, input().split()))
    adjacency_matrix[start - 1][end - 1] = (cost, False)
    adjacency_matrix[end - 1][start - 1] = (cost, False)
    original_pipes.append((start - 1, end - 1))

# Use Prim's algorithm to get MST
current_node = [False for _ in range(buildings)]
current_node[0] = True

for i in range(buildings - 1):
    minimum_cost = inf

    start = 0
    end = 0
    for j in range(buildings):
        if current_node[j]:
            for k in range(buildings):
                if (not current_node[k]) and (adjacency_matrix[j][k] is not None):
                    if minimum_cost > adjacency_matrix[j][k][0]:
                        minimum_cost = adjacency_matrix[j][k][0]
                        start = j
                        end = k

    pipes_needed.append((start, end))
    pipes_needed.append((end, start))

    current_node[end] = True

# Count switches
for connection in original_pipes:
    if (connection in pipes_needed) and (not adjacency_matrix[connection[0]][connection[1]][1]):
        pipe_activations += 1
    elif (connection not in pipes_needed) and (adjacency_matrix[connection[0]][connection[1]][1]):
        pipe_deactivations += 1

print(max(pipe_activations, pipe_deactivations))

"""
4 4 0
1 2 1
2 3 2
3 4 1
4 1 1
"""

