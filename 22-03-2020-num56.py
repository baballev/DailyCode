# Given a non oriented graph and an integer k, find
# wether each vertex in the graph can be colored so that
# Each adjacent vertex does not have the same color using k colors
# The graph is represented as an adjacency matrix. Since we do not care
# About the weights of the link between the vertices, we will consider
# That the graph is a matrix of boolean and that graph[i][j] is true if and only if there is a link between vertex i and j.
# We assume that the diagonal is false because otherwise, some vertices are neighbours of themselves and so we can't color the graph as wanted.
# We could check wether the diagonal is false or not if needed.

# Draft:
# DFS with backtrackinng?


def colorer(graph, k, color=[]):
    n = len(graph)
    if not color: color = [-1]*n
    elif -1 not in color: return True # All vertices have been colored with success and so we are propagating the success through the recursive calls
    for i in range(n): # For each vertex in the graph
        if color[i] == -1: # Check if the vertex has already been colored
            for l in range(k): # For each color available
                found_color = False
                for j in range(n): # Check if there is an adjacent vertex that has already been colored in the color l.
                    if graph[i][j]:
                        if color[j] == l:
                            found_color = True
                if not found_color: # if there is no adjacent vertex with color l, color the i'th vertex in l and keep coloring for next vertex.
                    new_color = color.copy()
                    new_color[i] = l
                    t = colorer(graph, k, new_color) 
                    if t: return t
            return False

test1 = [[0 for _ in range(11)],
         [0 for _ in range(11)],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
print(colorer(test1, 3))

test2 = [[0 for _ in range(12)],
         [0 for _ in range(12)],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]]
print(colorer(test2, 3))

