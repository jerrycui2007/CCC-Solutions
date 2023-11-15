# https://dmoj.ca/submission/5928229
gates = int(input())
planes = int(input())

current_gates = [0 for _ in range(gates + 1)]  # zero means that numbered gate is empty, non-zero means occupied

plane_gates = []
for _ in range(planes):
    plane_gates.append(int(input()))

has_space = True
total_planes = 0

while has_space:
    current_plane = plane_gates.pop(0)
    while current_plane > 0 and current_gates[current_plane] > 0:
        current_gates[current_plane] += 1
        current_plane -= current_gates[current_plane] - 1
    if current_plane <= 0:
        has_space = False
    else:
        current_gates[current_plane] = 1
        total_planes += 1

print(total_planes)

"""
4
3
4
1
1
"""



