# https://dmoj.ca/problem/ccc01j1
# Just use for loops to print out the bow tie.
height = int(input())

for i in range(1, height + 1, 2):
    print("*" * i + " " * (height * 2 - 2 * i) + "*" * i)
for i in range(height - 2, 0, -2):
    print("*" * i + " " * (height * 2 - 2 * i) + "*" * i)
