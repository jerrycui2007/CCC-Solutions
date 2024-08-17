# https://dmoj.ca/problem/ccc04j1
from math import floor, sqrt

squares = int(input())
print("The largest square has side length {0}.".format(floor(sqrt(squares))))
