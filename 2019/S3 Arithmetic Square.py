# https://dmoj.ca/problem/ccc19s3
square = [input().split(), input().split(), input().split()]
blank_spaces = 0

# convert to integers and count blank spaces
for row in square:
    for column in range(3):
        if row[column] != "X":
            row[column] = int(row[column])
        else:
            blank_spaces += 1

while blank_spaces > 0:
    # If two out of three numbers in a line are filled in, the last number can be calculated
    # Since they form an arithmetic sequence [a, b, c], we can use the formulas a = 2b - c, b = (a + c)/2, c = 2b - a
    # If we go an entire loop without filling in a square, there are no forced moves, so we can replace an X with an
    # arbitrary number (i.e. 0)
    filled_in_blank = False
    for row in range(3):
        for column in range(3):
            if square[row][column] == "X":
                # See if the column has two numbers
                if row == 0 and type(square[1][column]) == type(square[2][column]) == int:
                    square[row][column] = 2 * square[1][column] - square[2][column]
                    blank_spaces -= 1
                    filled_in_blank = True
                elif row == 1 and type(square[0][column]) == type(square[2][column]) == int:
                    square[row][column] = int((square[0][column] + square[2][column]) / 2)
                    blank_spaces -= 1
                    filled_in_blank = True
                elif row == 2 and type(square[0][column]) == type(square[1][column]) == int:
                    square[row][column] = 2 * square[1][column] - square[0][column]
                    blank_spaces -= 1
                    filled_in_blank = True
                # See if the row has two numbers
                elif column == 0 and type(square[row][1]) == type(square[row][2]) == int:
                    square[row][column] = 2 * square[row][1] - square[row][2]
                    blank_spaces -= 1
                    filled_in_blank = True
                elif column == 1 and type(square[row][0]) == type(square[row][2]) == int:
                    square[row][column] = int((square[row][0] + square[row][2]) / 2)
                    blank_spaces -= 1
                    filled_in_blank = True
                elif column == 2 and type(square[row][0]) == type(square[row][1]) == int:
                    square[row][column] = 2 * square[row][1] - square[row][0]
                    blank_spaces -= 1
                    filled_in_blank = True

    if not filled_in_blank:
        for row in range(3):
            for column in range(3):
                if square[row][column] == "X" and not filled_in_blank:
                    square[row][column] = 0
                    filled_in_blank = True
                    blank_spaces -= 1

for row in square:
    print(*row)
