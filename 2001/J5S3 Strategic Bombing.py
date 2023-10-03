# https://dmoj.ca/problem/ccc01s3
# Use a graph to store the roads, and then take away each road in turn, and do a breadth-first search to see if they
# are still connected
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
        map[road[1]].append(road[0])  # all roads are two-way


# Test every road to see, if removed, would cut off A to B
def is_connected(graph, start, end):
    # Checks if the start and end point are connected
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

