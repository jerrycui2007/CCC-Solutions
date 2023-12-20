# https://dmoj.ca/problem/ccc03s1
square = 1

number = int(input())
while number != 0:
    if number + square == 100:
        print("You Win!")
        break
    elif number + square < 100:
        square += number
        if square == 54:
            square = 19
        if square == 90:
            square = 48
        if square == 99:
            square = 77
        if square == 9:
            square = 34
        if square == 40:
            square = 64
        if square == 67:
            square = 86
    else:
        pass

    print("You are now on square " + str(square))
    number = int(input())

if number == 0:
    print("You Quit!")