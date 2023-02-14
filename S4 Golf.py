# https://dmoj.ca/problem/ccc00s4
distance = int(input())

club_strengths = []
for _ in range(int(input())):
    club_strengths.append(int(input()))

# Check to see if it is possible to make the distance with the given clubs
sums_list = [False] * (distance + 1)  # sums_list[i] will contain a bool of whether i - 1 is possible
sums_list[0] = True  # it is always possible to make 0

for i in range(0, distance + 1):
    if sums_list[i]:  # if the i - 1 can indeed be made by the numbers
        for number in club_strengths:
            if i + number <= len(sums_list) - 1:  # If the next possible sum is in the sums_list
                sums_list[i + number] = True

if sums_list[distance]:  # can make the distance with the clubs
    # Find the minimum number of strokes to make the distance
    lookup = [0] * (distance + 1)  # the value at lookup[i] stores the amount of coins needed to make that value

    for i in range(1, distance + 1):  # non-zero indexed
        lookup[i] = 9e9  # any large value
        for value in club_strengths:
            if i >= value:  # i.e. while checking the 5m club, the distance has to be at least 5m
                lookup[i] = min(lookup[i], lookup[i - value] + 1)  # + 1 as that requires one more stroke

    strokes_required = lookup[distance]
    print("Roberta wins in {0} strokes.".format(strokes_required))

else:
    print("Roberta acknowledges defeat.")
