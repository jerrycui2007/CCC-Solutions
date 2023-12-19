# https://dmoj.ca/problem/ccc03j2
from math import inf
pictures = int(input())

while pictures != 0:
    minimum_perimeter = inf
    lowest_i = 1

    for i in range(1, pictures):
        if pictures % i == 0: # integer dimensions
            perimeter = 2 * i + 2 * (pictures / i)
            if perimeter < minimum_perimeter:
                minimum_perimeter = perimeter
                lowest_i = i

    if minimum_perimeter == inf:  # special case of 1 picture
        minimum_perimeter = 1

    print("Minimum perimeter is {0} with dimensions {1} x {2}".format(int(minimum_perimeter), lowest_i, int(pictures / lowest_i)))

    pictures = int(input())

