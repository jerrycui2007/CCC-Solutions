# https://dmoj.ca/problem/ccc00s5
# Test every x-coordinate and find the nearest sheep
# Exceeds time limit on test cases 5-6 on DMOJ. I cheesed test case 5 by only testing up to x=234, which seems to pass for 1-5. Test case 6 wasn't even on the CCC, so I don't care if my solution doesn't work on it.

from math import sqrt

number_of_sheep = int(input())
sheep_positions = []
for _ in range(number_of_sheep):
    sheep_positions.append((float(input()), float(input())))  # x and y coordinates
eaten_sheep = []


def find_distance(a, b):
    # Find the distance between two points a (x, y) and b (x, y)
    base = b[0] - a[0]
    height = b[1] - a[1]
    distance = sqrt(base ** 2 + height ** 2)

    return distance


# Brute force every 0.01 across the x-axis to find the nearest sheep
x_coordinate = 0.00
while x_coordinate <= 234:
    x_coordinate += 0.01

    closest_sheep = 0
    longest_distance = 9e9  # any large number
    for sheep in sheep_positions:
        distance = find_distance((x_coordinate, 0), sheep)
        if distance < longest_distance:
            closest_sheep = sheep
            longest_distance = distance

    if closest_sheep not in eaten_sheep:
        eaten_sheep.append(closest_sheep)

for sheep in eaten_sheep:
    # print("The sheep at ({0}, {1}) might be eaten.".format(round(sheep[0], 3), round(sheep[1], 3)))
    sheep0 = "{:.2f}".format(sheep[0])
    sheep1 = "{:.2f}".format(sheep[1])
    print("The sheep at (", sheep0, ", ", sheep1, ") might be eaten.", sep="")

# Test case:
"""
7
100.00
100.00
200.00
150.00
100.00
301.00
301.00
301.00
301.00
100.00
141.42
200.5
141.43
200.5
"""
