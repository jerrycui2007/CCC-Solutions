# https://dmoj.ca/problem/ccc12s1
# Use combinations(N, R) formula, and memoization to save time

goal_scorer_number = int(input())

memoization = [0 for i in range(100)]
memoization[0] = 1  # 0! = 1


def factorial(x):
    if memoization[x] == 0:  # factorial has not been calculated yet
        return x * factorial(x - 1)
    else:
        return memoization[x]



def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


if goal_scorer_number - 3 >= 1:
    print(int(combinations(goal_scorer_number - 1, 3)))
else:
    print(0)