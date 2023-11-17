# https://dmoj.ca/problem/ccc02s3
# Doesn't do last two test cases on DMOJ, but they aren't CCC official cases anyways
rows = int(input())
columns = int(input())

field = []
for _ in range(rows):
    field.append(list(input()))

number_of_moves = int(input())
moves = []
for _ in range(number_of_moves):
    moves.append(input())

directions = ["North", "East", "South", "West"]


class ObstacleError(Exception):
    pass


for start_row in range(rows):
    for start_column in range(columns):
        for orientation in (0, 1, 2, 3):  # orientation % 4 gives direction: 0 = North, 1 = East, 2 = South, 3 = West
            row = start_row
            column = start_column
            start_orientation = orientation
            if field[row][column] in (".", "*"):
                try:
                    for move in moves:
                        if move == "L":
                            orientation -= 1
                        elif move == "R":
                            orientation += 1
                        else:  # move == "F":
                            if directions[orientation % 4] == "North":
                                row -= 1
                            elif directions[orientation % 4] == "East":
                                column += 1
                            elif directions[orientation % 4] == "South":
                                row += 1
                            else:  # directions[orientation % 4] == "West":
                                column -= 1
                            if field[row][column] == "X":
                                raise ObstacleError
                    if row >= 0 and column >= 0:
                        field[row][column] = "*"
                except:
                    pass

for row in field:
    output_string = ""
    for char in row:
        output_string += char
    print(output_string)