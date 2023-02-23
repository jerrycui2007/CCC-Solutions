# https://dmoj.ca/problem/ccc01s3
# Use a graph to store the roads, and then "reform" the graph so
# all nodes point towards B and away from A. Then, take away each
# road and see if A and B are still connected using a breadth-first
# search
map = {"A": [],
       "B": [],
       "C": [],
       "D": [],
       "E": [],
       "F": [],
       "G": [],
       "H": [],
       "I": [],
       "J": [],
       "K": [],
       "L": [],
       "M": [],
       "N": [],
       "O": [],
       "P": [],
       "Q": [],
       "R": [],
       "S": [],
       "T": [],
       "U": [],
       "V": [],
       "W": [],
       "X": [],
       "Y": [],
       "Z": []}
disconnecting_roads = []

while True:
    road = input()
    if road == "**":
        break
    else:
        map[road[0]].append(road[1])
        map[road[1]].append(road[0])  # all roads are two-way!


# Make this graph directed, by pointing all edges towards B
def reform_graph(point):
    """ (dict, str) -> dict
        Redirects a graph by making edges only point towards the start node, using a recursive function
    """
    points_to_reform = []

    if point == "A":  # point A is the first point, so it cannot be reformed
        pass
    else:
        for node in map:
            if point in map[node]:  # for every point that each point in the map points to
                points_to_reform.append(node)  # that point has to be reformed

        for node in points_to_reform:
            if node in map[point]:  # only need to reform a node if it is still linked to
                if point == "B":
                    map[point].remove(node)
                    reform_graph(node)  # reform the node by recursively calling function
                else:
                    if "B" not in map[node]:  # if the point isn't B, then we have to make sure it doesn't link
                        map[point].remove(node)  # to B
                        reform_graph(node)


reform_graph("B")


# Test every road to see, if removed, would cut off A to B
def is_connected(graph, start, end):
    """ (dict, str, str) -> bool
        Checks if two points are connected, using a modified breadth first search
    """
    visited = set()
    visited.add(start)

    queue = [start]

    while len(queue) > 0:
        target = queue.pop(0)
        for neighbor in graph[target]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    if end in visited:
        return True
    else:
        return False


# Generate list of all roads
roads = []
for point in map:  # loop through the map to create a list of all roads, in the proper direction
    for neighbor in map[point]:
        roads.append(point + neighbor)

for road in roads:
    map[road[0]].remove(road[1])
    if not is_connected(map, "A", "B"):
        disconnecting_roads.append(road)
    map[road[0]].append(road[1])

for disconnecting_road in disconnecting_roads:
    print(disconnecting_road[0] + disconnecting_road[1])
print("There are {0} disconnecting roads.".format(len(disconnecting_roads)))

"""
AC
AD
AE
CE
CF
ED
GF
BG
HB
GH
**
"""
"""
CF
GF
There are 2 disconnecting roads.
"""
