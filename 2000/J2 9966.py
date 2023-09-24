# https://dmoj.ca/problem/ccc00j2
start = int(input())
end = int(input())


# Check if a number is same when flipped
def flip_number(num):
    str_num = str(num)
    output = ""

    for char in reversed(str_num):
        if char == "1":
            output += "1"
        elif char == "6":
            output += "9"
        elif char == "8":
            output += "8"
        elif char == "9":
            output += "6"
        elif char == "0":
            output += "0"
        else:
            return False

    if output == str_num:
        return True
    else:
        return False


total = 0
for i in range(start, end + 1):
    if flip_number(i):
        total += 1

print(total)
