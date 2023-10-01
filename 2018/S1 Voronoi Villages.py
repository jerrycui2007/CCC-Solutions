# https://dmoj.ca/problem/ccc18s1
from math import trunc

number_of_villages = int(input())
village_positions = []
smallest_size = 9999999999  # any large number

for _ in range(number_of_villages):
    village_positions.append(int(input()))

village_positions.sort()

for i in range(1, number_of_villages - 1):  # loop through all villages except the first and last
    # Distance between midpoints of adjacent villages
    size = ((village_positions[i] - village_positions[i - 1]) / 2) + ((village_positions[i + 1] - village_positions[i]) / 2)
    if size < smallest_size:
        smallest_size = size

smallest_size = int(smallest_size * 10) / 10  # truncate to one decimal place
print(smallest_size)
