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


def bfs(graph, target, visited):
    for neighbor in graph[target]:
        if neighbor not in visited:
            visited.add(neighbor)
            bfs(graph, neighbor, visited)

    return visited


for pair in pairs:
    connected = bfs(weblinks, pair[0], set())
    if pair[1] in connected:
        print("Can surf from {0} to {1}.".format(pair[0], pair[1]))
    else:
        print("Can't surf from {0} to {1}.".format(pair[0], pair[1]))
