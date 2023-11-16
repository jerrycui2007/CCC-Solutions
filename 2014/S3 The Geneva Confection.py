# https://dmoj.ca/problem/ccc14s3
test_cases = int(input())

for _ in range(test_cases):
    number_of_ingredients = int(input())

    mountain_top = []  # last item is item on bottom
    branch = [0]  # last item is item on top
    lake = [0]  # last item is last item to enter

    target = [i for i in range(0, number_of_ingredients + 1)]

    for _ in range(number_of_ingredients):
        mountain_top.append(int(input()))

    while True:
        if lake == target:
            print("Y")
            break

        if len(mountain_top) > 0:
            if mountain_top[-1] == lake[-1] + 1:
                lake.append(mountain_top.pop(-1))
                continue

        if len(branch) > 0:
            if branch[-1] == lake[-1] + 1:
                lake.append(branch.pop(-1))
                continue

        if len(mountain_top) > 0:
            branch.append(mountain_top.pop(-1))
            continue

        print("N")
        break

"""
2
4
2
3
1
4
4
4
1
3
2
"""
