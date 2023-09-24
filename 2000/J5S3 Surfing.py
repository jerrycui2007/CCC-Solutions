# https://dmoj.ca/problem/ccc00s3
# The websites can be represented in a graph and then use a depth-first search to check for connections

n = int(input())

weblinks = {}

for _ in range(n):
    link = input()
    weblinks[link] = []

    while True:
        line = input()
        if line == "</HTML>":
            break

        checked_chars = ""
        url = ""
        for char in line:
            checked_chars += char

            if '<A HREF="' in checked_chars:
                if char != '"':
                    url += char
                if char == '"' and len(url) > 1:
                    weblinks[link].append(url)
                    if url not in weblinks:
                        weblinks[url] = []
                    print("Link from " + link + " to " + url)
                    checked_chars = ""
                    url = ""

pairs = []

while True:
    line = input()
    if line == "The End":
        break
    else:
        pairs.append((line, input()))


def depth_first_search(graph, target, visited):
    for neighbor in graph[target]:
        if neighbor not in visited:
            visited.add(neighbor)
            depth_first_search(graph, neighbor, visited)

    return visited


for pair in pairs:
    connected = depth_first_search(weblinks, pair[0], set())
    if pair[1] in connected:
        print("Can surf from {0} to {1}.".format(pair[0], pair[1]))
    else:
        print("Can't surf from {0} to {1}.".format(pair[0], pair[1]))
