# https://dmoj.ca/problem/ccc19s2
from math import sqrt

test_cases = int(input())

numbers = []
for _ in range(test_cases):
    numbers.append(int(input()))


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


for number in numbers:
    # increment by positive and negative one so their average is always the same
    lower_number = number - 1
    higher_number = number + 1

    while (not is_prime(lower_number)) or (not is_prime(higher_number)):
        lower_number -= 1
        higher_number += 1

    print(lower_number, higher_number)
